from __future__ import annotations

import json
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app


class TestApiV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)
        cls.data_file = (
            Path(__file__).resolve().parents[3]
            / "data"
            / "elearning"
            / "pruefungen_v1.json"
        )
        cls.audit_file = (
            Path(__file__).resolve().parents[3]
            / "data"
            / "elearning"
            / "audit_log_v1.jsonl"
        )
        cls.plugins_file = (
            Path(__file__).resolve().parents[3]
            / "data"
            / "elearning"
            / "plugins_v1.json"
        )
        cls.plugins_baseline = cls.plugins_file.read_text(encoding="utf-8")

    def setUp(self) -> None:
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.data_file.write_text("[]\n", encoding="utf-8")
        self.audit_file.write_text("", encoding="utf-8")
        self.plugins_file.write_text(self.plugins_baseline, encoding="utf-8")

    def test_plugins_list(self) -> None:
        response = self.client.get(
            "/api/v1/plugins",
            headers=self._headers(role="review", user="reviewer-plugins"),
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreaterEqual(len(data), 2)

        ids = {item["id"] for item in data}
        self.assertIn("pruefungsmodul", ids)
        self.assertIn("drawio-extension", ids)

    def test_plugins_list_filter_enabled(self) -> None:
        self.client.patch(
            "/api/v1/plugins/drawio-extension/activation",
            json={"enabled": False},
            headers=self._headers(role="admin", user="admin-filter"),
        )

        response_enabled = self.client.get(
            "/api/v1/plugins?enabled=true",
            headers=self._headers(role="review", user="reviewer-plugins"),
        )
        self.assertEqual(response_enabled.status_code, 200)
        ids_enabled = {item["id"] for item in response_enabled.json()}
        self.assertIn("pruefungsmodul", ids_enabled)
        self.assertNotIn("drawio-extension", ids_enabled)

        response_disabled = self.client.get(
            "/api/v1/plugins?enabled=false",
            headers=self._headers(role="review", user="reviewer-plugins"),
        )
        self.assertEqual(response_disabled.status_code, 200)
        ids_disabled = {item["id"] for item in response_disabled.json()}
        self.assertIn("drawio-extension", ids_disabled)

    def test_plugins_get_not_found(self) -> None:
        response = self.client.get(
            "/api/v1/plugins/unbekanntes-plugin",
            headers=self._headers(role="review", user="reviewer-plugins"),
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["code"], "NOT_FOUND")

    def test_plugin_activation_requires_admin(self) -> None:
        response = self.client.patch(
            "/api/v1/plugins/pruefungsmodul/activation",
            json={"enabled": False},
            headers=self._headers(role="review", user="reviewer-plugins"),
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()["code"], "FORBIDDEN")

    def test_plugin_activation_updates_state(self) -> None:
        disable_response = self.client.patch(
            "/api/v1/plugins/pruefungsmodul/activation",
            json={"enabled": False},
            headers=self._headers(role="admin", user="admin-1"),
        )
        self.assertEqual(disable_response.status_code, 200)
        self.assertFalse(disable_response.json()["enabled"])
        self.assertEqual(disable_response.json()["status"], "inactive")

        get_response = self.client.get(
            "/api/v1/plugins/pruefungsmodul",
            headers=self._headers(role="review", user="reviewer-plugins"),
        )
        self.assertEqual(get_response.status_code, 200)
        self.assertFalse(get_response.json()["enabled"])

    @staticmethod
    def _headers(role: str = "admin", user: str = "tester") -> dict[str, str]:
        return {"X-Role": role, "X-User-Id": user}

    def test_health_endpoint(self) -> None:
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_pruefung_create_and_get(self) -> None:
        payload = {
            "titel": "Testklausur API v1",
            "jahrgangsstufe": "2",
            "fach": "Informatik",
            "zeit_minuten": 90,
            "status": "draft",
            "anforderungsbereiche": {"ab1": 30, "ab2": 40, "ab3": 30},
            "themen": ["Sortieren", "Suchen"],
            "aufgaben": [
                {"aufgabe_id": "A1", "titel": "Bubble Sort", "punkte": 10},
                {"aufgabe_id": "A2", "titel": "Lineare Suche", "punkte": 8},
            ],
        }

        create_response = self.client.post(
            "/api/v1/pruefungen",
            json=payload,
            headers=self._headers(role="autor", user="lehrkraft-1"),
        )
        self.assertEqual(create_response.status_code, 200)

        pruefung_id = create_response.json()["id"]
        get_response = self.client.get(
            f"/api/v1/pruefungen/{pruefung_id}",
            headers=self._headers(role="review", user="reviewer-1"),
        )
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.json()["titel"], payload["titel"])

        persisted = json.loads(self.data_file.read_text(encoding="utf-8"))
        self.assertEqual(len(persisted), 1)

    def test_error_format_contains_trace_id(self) -> None:
        response = self.client.get("/api/milestones/unbekannt")
        self.assertEqual(response.status_code, 404)
        body = response.json()

        self.assertIn("code", body)
        self.assertIn("message", body)
        self.assertIn("details", body)
        self.assertIn("traceId", body)
        self.assertIn("X-Trace-Id", response.headers)

    def test_rbac_blocks_without_role(self) -> None:
        payload = {
            "titel": "Nicht erlaubt",
            "jahrgangsstufe": "2",
            "fach": "Informatik",
            "zeit_minuten": 60,
            "status": "draft",
            "anforderungsbereiche": {"ab1": 30, "ab2": 40, "ab3": 30},
            "themen": [],
            "aufgaben": [],
        }
        response = self.client.post("/api/v1/pruefungen", json=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()["code"], "FORBIDDEN")

    def test_audit_log_written_on_create(self) -> None:
        payload = {
            "titel": "Audit Test",
            "jahrgangsstufe": "2",
            "fach": "Informatik",
            "zeit_minuten": 60,
            "status": "draft",
            "anforderungsbereiche": {"ab1": 30, "ab2": 40, "ab3": 30},
            "themen": ["Suche"],
            "aufgaben": [],
        }
        response = self.client.post(
            "/api/v1/pruefungen",
            json=payload,
            headers=self._headers(role="autor", user="lehrkraft-2"),
        )
        self.assertEqual(response.status_code, 200)

        lines = [line for line in self.audit_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertGreaterEqual(len(lines), 1)


if __name__ == "__main__":
    unittest.main()
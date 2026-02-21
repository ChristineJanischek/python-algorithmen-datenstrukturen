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

    def setUp(self) -> None:
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.data_file.write_text("[]\n", encoding="utf-8")

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

        create_response = self.client.post("/api/v1/pruefungen", json=payload)
        self.assertEqual(create_response.status_code, 200)

        pruefung_id = create_response.json()["id"]
        get_response = self.client.get(f"/api/v1/pruefungen/{pruefung_id}")
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


if __name__ == "__main__":
    unittest.main()
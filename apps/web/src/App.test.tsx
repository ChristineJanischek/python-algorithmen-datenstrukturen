import { render, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import App from "./App";

describe("App", () => {
  beforeEach(() => {
    vi.stubGlobal(
      "fetch",
      vi.fn(async (input: RequestInfo | URL) => {
        const url = String(input);

        if (url.includes("/api/tasks")) {
          return {
            json: async () => [
              {
                id: "t1",
                title: "Bubble Sort Aufgabe",
                description: "Sortiere ein Array",
                struktogramm: "L2_Bubble_Sort",
                tags: ["Sortieren"],
              },
            ],
          } as Response;
        }

        if (url.includes("/api/milestones/ms1")) {
          return {
            json: async () => ({
              id: "ms1",
              title: "Meilenstein 1",
              description: "Listen, Sortieren, Suchen",
              content: "Inhalt",
            }),
          } as Response;
        }

        if (url.includes("/api/operatorenliste")) {
          return {
            json: async () => ({ content: "Operatorenliste" }),
          } as Response;
        }

        if (url.includes("/api/v1/plugins")) {
          return {
            ok: true,
            json: async () => [
              {
                id: "pruefungsmodul",
                name: "Prüfungsmodul",
                enabled: true,
                status: "active",
                version: "0.1.0",
              },
            ],
          } as Response;
        }

        return { json: async () => ({}) } as Response;
      })
    );
  });

  afterEach(() => {
    vi.unstubAllGlobals();
    vi.clearAllMocks();
  });

  it("rendert Basislayout und lädt Aufgaben", async () => {
    render(<App />);

    expect(screen.getByText("Struktogramm E-Learning")).toBeInTheDocument();

    const taskEntries = await screen.findAllByText("Bubble Sort Aufgabe");
    expect(taskEntries.length).toBeGreaterThan(0);

    expect(screen.getByText("Code-Box")).toBeInTheDocument();
    expect(screen.getByText("Plugins (Erweiterungen)")).toBeInTheDocument();
    expect(screen.getByText("Prüfungsmodul")).toBeInTheDocument();
  });
});
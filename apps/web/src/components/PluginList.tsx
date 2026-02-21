import { useEffect, useState } from "react";

const API_BASE = "http://localhost:8000";
const USER_ROLE = (import.meta.env.VITE_USER_ROLE ?? "review").toLowerCase();
const USER_ID = import.meta.env.VITE_USER_ID ?? "web-client";

interface PluginItem {
  id: string;
  name: string;
  enabled: boolean;
  status: string;
  version: string;
}

export default function PluginList() {
  const [plugins, setPlugins] = useState<PluginItem[]>([]);
  const [error, setError] = useState<string>("");
  const [pendingPluginId, setPendingPluginId] = useState<string>("");
  const isAdmin = USER_ROLE === "admin";

  useEffect(() => {
    fetch(`${API_BASE}/api/v1/plugins`, {
      headers: {
        "X-Role": USER_ROLE,
        "X-User-Id": USER_ID,
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Plugins konnten nicht geladen werden.");
        }
        return response.json();
      })
      .then((data: PluginItem[]) => setPlugins(data))
      .catch((fetchError: Error) => setError(fetchError.message));
  }, []);

  async function togglePluginActivation(plugin: PluginItem) {
    if (!isAdmin) {
      return;
    }

    setPendingPluginId(plugin.id);
    setError("");

    try {
      const response = await fetch(`${API_BASE}/api/v1/plugins/${plugin.id}/activation`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          "X-Role": USER_ROLE,
          "X-User-Id": USER_ID,
        },
        body: JSON.stringify({ enabled: !plugin.enabled }),
      });

      if (!response.ok) {
        throw new Error("Plugin-Status konnte nicht aktualisiert werden.");
      }

      const updatedPlugin = (await response.json()) as PluginItem;
      setPlugins((previous) =>
        previous.map((item) => (item.id === updatedPlugin.id ? updatedPlugin : item))
      );
    } catch (updateError) {
      const message = updateError instanceof Error ? updateError.message : "Unbekannter Fehler";
      setError(message);
    } finally {
      setPendingPluginId("");
    }
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div className="plugin-list">
      {plugins.map((plugin) => (
        <div className="plugin-item" key={plugin.id}>
          <strong>{plugin.name}</strong>
          <span>
            Status: {plugin.enabled ? "aktiv" : "inaktiv"} ({plugin.status})
          </span>
          <span>Version: {plugin.version}</span>
          {isAdmin && (
            <button
              className="plugin-toggle"
              type="button"
              onClick={() => void togglePluginActivation(plugin)}
              disabled={pendingPluginId === plugin.id}
            >
              {pendingPluginId === plugin.id
                ? "Aktualisiere..."
                : plugin.enabled
                  ? "Deaktivieren"
                  : "Aktivieren"}
            </button>
          )}
        </div>
      ))}
    </div>
  );
}
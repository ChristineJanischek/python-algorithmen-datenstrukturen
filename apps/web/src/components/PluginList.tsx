import { useEffect, useState } from "react";

const API_BASE = "http://localhost:8000";

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

  useEffect(() => {
    fetch(`${API_BASE}/api/v1/plugins`, {
      headers: {
        "X-Role": "review",
        "X-User-Id": "web-client",
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
        </div>
      ))}
    </div>
  );
}
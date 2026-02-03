import { useEffect, useState } from "react";

const API_BASE = "http://localhost:8000";

export default function OperatorList() {
  const [content, setContent] = useState<string>("");

  useEffect(() => {
    fetch(`${API_BASE}/api/operatorenliste`)
      .then((response) => response.json())
      .then((data: { content: string }) => setContent(data.content));
  }, []);

  return (
    <details>
      <summary>Operatorenliste anzeigen</summary>
      <pre className="markdown">{content}</pre>
    </details>
  );
}

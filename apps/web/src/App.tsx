import { useEffect, useState } from "react";
import CodeBox from "./components/CodeBox";
import TaskList from "./components/TaskList";
import TaskDetail from "./components/TaskDetail";
import OperatorList from "./components/OperatorList";

interface Task {
  id: string;
  title: string;
  description: string;
  struktogramm: string;
  tags: string[];
}

interface Milestone {
  id: string;
  title: string;
  description: string;
  content?: string;
  operatorListPath?: string;
}

const API_BASE = "http://localhost:8000";

export default function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [selectedTask, setSelectedTask] = useState<Task | null>(null);
  const [milestone, setMilestone] = useState<Milestone | null>(null);
  useEffect(() => {
    fetch(`${API_BASE}/api/tasks?milestone=ms1`)
      .then((response) => response.json())
      .then((data: Task[]) => {
        setTasks(data);
        if (data.length > 0) {
          setSelectedTask(data[0]);
        }
      });

    fetch(`${API_BASE}/api/milestones/ms1`)
      .then((response) => response.json())
      .then((data: Milestone) => setMilestone(data));
  }, []);

  return (
    <div className="layout">
      <aside className="sidebar">
        <h1>Struktogramm E-Learning</h1>
        <p className="subtitle">Meilenstein 1: Listen, Sortieren, Suchen</p>
        <TaskList
          tasks={tasks}
          selectedTaskId={selectedTask?.id}
          onSelect={setSelectedTask}
        />
      </aside>

      <main className="content">
        <section className="panel">
          <h2>{milestone?.title ?? "Meilenstein"}</h2>
          <p>{milestone?.description}</p>
          {milestone?.content && (
            <details>
              <summary>Aufgabenpaket anzeigen</summary>
              <pre className="markdown">{milestone.content}</pre>
            </details>
          )}
        </section>

        <section className="panel">
          <h2>Ausgewählte Aufgabe</h2>
          {selectedTask ? (
            <TaskDetail
              title={selectedTask.title}
              description={selectedTask.description}
              struktogramm={selectedTask.struktogramm}
            />
          ) : (
            <p>Keine Aufgabe ausgewählt.</p>
          )}
        </section>

        <section className="panel">
          <h2>Code-Box</h2>
          <CodeBox placeholder="Setze das Struktogramm in Code um..." />
        </section>

        <section className="panel">
          <h2>Operatorenliste</h2>
          <p>Diese Hilfestellung ist während der Bearbeitung immer verfügbar.</p>
          <OperatorList />
        </section>
      </main>
    </div>
  );
}

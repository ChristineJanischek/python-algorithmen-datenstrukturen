interface Task {
  id: string;
  title: string;
  description: string;
  struktogramm: string;
  tags: string[];
}

interface TaskListProps {
  tasks: Task[];
  selectedTaskId?: string;
  onSelect: (task: Task) => void;
}

export default function TaskList({ tasks, selectedTaskId, onSelect }: TaskListProps) {
  return (
    <div className="task-list">
      {tasks.map((task) => (
        <button
          key={task.id}
          className={`task-item ${selectedTaskId === task.id ? "active" : ""}`}
          onClick={() => onSelect(task)}
          type="button"
        >
          <span className="task-title">{task.title}</span>
          <span className="task-description">{task.description}</span>
        </button>
      ))}
    </div>
  );
}

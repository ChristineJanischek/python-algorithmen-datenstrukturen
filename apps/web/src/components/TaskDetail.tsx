interface TaskDetailProps {
  title?: string;
  description?: string;
  struktogramm?: string;
}

export default function TaskDetail({ title, description, struktogramm }: TaskDetailProps) {
  return (
    <div>
      <h3>{title ?? ""}</h3>
      <p>{description ?? ""}</p>
      {struktogramm && (
        <p className="meta">
          Struktogramm: <span>{struktogramm}</span>
        </p>
      )}
    </div>
  );
}

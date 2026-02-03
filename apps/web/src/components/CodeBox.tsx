interface CodeBoxProps {
  placeholder?: string;
}

export default function CodeBox({ placeholder }: CodeBoxProps) {
  return (
    <div className="codebox">
      <textarea
        className="codebox-textarea"
        placeholder={placeholder}
        spellCheck={false}
      />
    </div>
  );
}

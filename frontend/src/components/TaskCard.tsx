
import { useState } from "react";
import type { Task } from "../types/task";

interface TaskCardProps {
  task: Task;
}

export default function TaskCard({ task }: TaskCardProps) {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <article>
      <button
        type="button"
        onClick={() => setIsExpanded((prev) => !prev)}
        aria-expanded={isExpanded}
      >
        <span>{task.title}</span>
        <span>Status: {task.status}</span>
      </button>

      {isExpanded && (
        <div>
          <p>Description: {task.description}</p>
          <p>
            Created: {new Date(task.created_at).toLocaleString()}
          </p>
          <p>
            Updated: {new Date(task.updated_at).toLocaleString()}
          </p>
        </div>
      )}
    </article>
  );
}

import { useEffect, useState } from "react";
import { getTasks } from "../services/tasksApi";
import type { Task } from "../types/task";
import TaskList from "../components/TaskList";

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;

    async function loadTasks() {
      try {
        const data = await getTasks();

        if (active) {
          setTasks(data);
        }
      } catch {
        if (active) {
          setError("Failed to load tasks");
        }
      } finally {
        if (active) {
          setLoading(false);
        }
      }
    }

    loadTasks();

    return () => {
      active = false;
    };
  }, []);

  if (loading) {
    return <p>Loading tasks...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <main>
      <h1>My Tasks</h1>

      <TaskList tasks={tasks} />
    </main>
  );
}

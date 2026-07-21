import { useState, useEffect } from "react";
import { Trash, Check, Undo2 } from "lucide-react";

import { getTasks, createTask, updateTask, deleteTask } from "./api/taskApi";

function App() {
  const [title, setTitle] = useState("");
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    async function loadTasks() {
      try {
        const response = await getTasks();
        setTasks(response.data);
      } catch (error) {
        console.error(error);
      }
    }
    loadTasks();
  }, []);

  async function handleCreateTask() {
    if (!title.trim()) return;

    try {
      const response = await createTask({
        title,
        completed: false,
      });

      setTasks((prev) => [...prev, response.data]);
      setTitle("");
    } catch (error) {
      console.error(error);
    }
  }

  async function handleToggleTask(task) {
    try {
      const response = await updateTask(task.id, {
        completed: !task.completed,
      });

      setTasks((prev) =>
        prev.map((t) => (t.id === task.id ? response.data : t))
      );
    } catch (error) {
      console.error(error);
    }
  }

  async function handleDeleteTask(id) {
    try {
      await deleteTask(id);

      setTasks((prev) => prev.filter((task) => task.id !== id));
    } catch (error) {
      console.error(error);
    }
  }
  return (
    <main className="min-h-screen bg-slate-100 flex justify-center py-16">
      <div className="w-full max-w-xl bg-white rounded-xl shadow-md p-6">
        <h1 className="text-3xl font-bold mb-6 text-center">Task Manager</h1>

        <div className="flex gap-3 mb-8">
          <input
            type="text"
            placeholder="Digite uma tarefa..."
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="flex-1 rounded-lg border border-slate-300 px-4 py-2 outline-none focus:ring-2 focus:ring-blue-500"
          />

          <button
            onClick={handleCreateTask}
            className="bg-blue-600 text-white px-5 rounded-lg hover:bg-blue-700 transition"
          >
            Criar
          </button>
        </div>

        <div className="space-y-3">
          {tasks.length === 0 && (
            <p className="text-center text-slate-500">
              Nenhuma tarefa cadastrada.
            </p>
          )}

          {tasks.map((task) => (
            <div
              key={task.id}
              className="flex items-center justify-between rounded-lg border border-slate-200 p-4"
            >
              <span
                className={`flex-1 min-w-0 break-words ${
                  task.completed
                    ? "line-through text-slate-400"
                    : "text-slate-800"
                }`}
              >
                {task.title}
              </span>

              <div className="flex gap-2 ml-4 shrink-0">
                <button
                  onClick={() => handleToggleTask(task)}
                  className={`rounded px-1 py-1 text-sm transition cursor-pointer ${
                    task.completed ? "text-black/100" : "text-green-400"
                  }`}
                >
                  {task.completed ? (
                    <Undo2 strokeWidth={2} />
                  ) : (
                    <Check strokeWidth={3} />
                  )}
                </button>

                <button
                  onClick={() => handleDeleteTask(task.id)}
                  className="rounded py-1 text-sm text-red-400 transition cursor-pointer"
                >
                  <Trash />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}

export default App;

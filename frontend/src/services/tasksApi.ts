import axios from "axios";
import type { Task } from "../types/task";

const api = axios.create({
    baseURL: "http://127.0.0.1:3000",
});

export async function getTasks(): Promise<Task[]> {
    const response = await api.get<Task[]>("/tasks");
    return response.data;
}
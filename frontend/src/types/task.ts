export type TaskStatus = 
| 'pending'
| 'in-progress'
| 'completed';

export interface Task {
    id: number;
    title: string;
    description: string;
    status: TaskStatus;
    created_at: string;
    updated_at: string;
}

export interface CreateTask {
    title: string;
    description?: string;
}

export interface UpdateTask {
    title?: string;
    description?: string;
    status?: TaskStatus;
}
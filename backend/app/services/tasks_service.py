from datetime import datetime, timezone
from app.dal.tasks_dal import get_all_tasks, get_task_by_id, save_task, update_task_by_id, delete_task_by_id

def list_tasks():
    return get_all_tasks()

def find_task(task_id):
    return get_task_by_id(task_id)

def create_task(task_data):
    tasks = get_all_tasks()

    new_id = max([task['id'] for task in tasks], default=0) + 1

    now = datetime.now(timezone.utc).isoformat()

    new_task = {
        "id": new_id,
        "title": task_data["title"],
        "description": task_data["description"],
        "status": "pending",
        "created_at": now,
        "updated_at": now
    }

    return save_task(new_task)

def update_task(task_id, updates):
    now = datetime.now(timezone.utc).isoformat()

    updates["updated_at"] = now

    return update_task_by_id(task_id, updates)

def delete_task(task_id):
    return delete_task_by_id(task_id)
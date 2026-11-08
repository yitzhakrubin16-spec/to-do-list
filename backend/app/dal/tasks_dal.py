import json
from pathlib import Path


TASKS_FILE = Path(__file__).resolve().parent.parent / "data" / "tasks.json"

def get_all_tasks():
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        tasks = json.load(file)
    
    return tasks

def get_task_by_id(task_id):
    tasks = get_all_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None

def save_task(task):
    tasks = get_all_tasks()
    tasks.append(task)
    
    write_tasks_to_file(tasks)

    return task    

def update_task_by_id(task_id, updates):
    tasks = get_all_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task.update(updates)
            
            write_tasks_to_file(tasks)

            return task

    return None

def delete_task_by_id(task_id):
    tasks = get_all_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            
            write_tasks_to_file(tasks)
            
            return True

    return False    

def write_tasks_to_file(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
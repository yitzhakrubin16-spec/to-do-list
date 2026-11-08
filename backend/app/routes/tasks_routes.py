from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from app.schemas.task_schema import createTaskSchema, UpdateTaskSchema
from app.services.tasks_service import list_tasks, find_task, create_task, update_task, delete_task

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.get("/tasks")
def get_all_tasks():
    tasks = list_tasks()

    return jsonify(tasks), 200



@tasks_bp.get("/tasks/<int:task_id>")
def get_task_by_id(task_id):    
    task = find_task(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404
    else:
        return jsonify(task), 200

@tasks_bp.post("/tasks")
def create_task_route():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    try:
        validated_data = createTaskSchema.model_validate(data)
    except ValidationError as error:
        return jsonify({
            "error": "Validation error",
            "details": error.errors(
                include_input=False,
                include_context=False,
                include_url=False
            )
        }), 400

    task = create_task(validated_data.model_dump())

    return jsonify(task), 201

@tasks_bp.patch("/tasks/<int:task_id>")
def update_task_route(task_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    try:
        validated_data = UpdateTaskSchema.model_validate(data)
    
    except ValidationError as error:
        return jsonify({
            "error" : "Validation failed",
            "details": error.errors(
                include_input=False,
                include_context=False,
                include_url=False
            )
        }), 400

    updates = validated_data.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    if not updates:
        return jsonify({"error": "No fields to update"}), 400

    task = update_task(task_id, updates)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200

@tasks_bp.delete("/tasks/<int:task_id>")
def delete_task_route(task_id):
    deleted = delete_task(task_id)

    if not deleted:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted successfully"}), 200

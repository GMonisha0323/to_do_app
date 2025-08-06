from fastapi import APIRouter, HTTPException
from models import Todo
import services

router = APIRouter()

@router.get("/todos")
def get_todos():
    return services.get_all_todos()

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    todo = services.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos")
def create_todo(todo: Todo):
    return services.add_todo(todo.dict())

@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    updated = services.update_todo(todo_id, todo.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    deleted = services.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return deleted

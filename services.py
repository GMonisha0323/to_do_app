todos = []

def get_all_todos():
    return todos

def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return None

def add_todo(todo_data: dict):
    todos.append(todo_data)
    return todo_data

def update_todo(todo_id: int, new_data: dict):
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            todos[i].update(new_data)
            return todos[i]
    return None

def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            return todos.pop(i)
    return None

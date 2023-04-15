from fastapi import APIRouter, Path, Query, Body, HTTPException
from model import TodoItem, UpdateTodoItem, TodoItems
todo_router = APIRouter()

todos=[]

@todo_router.get("/todos", response_model=TodoItems)
async def get_todos() -> dict:
    return {"todos": todos}


@todo_router.get("/todos/{todo_id}")
async def get_todo(todo_id: int = Path(..., title="The ID of the todo item to get")) -> dict:
    todo = [todo for todo in todos if todo["id"] == todo_id]
    if todo:
        return {"todo": todo}
    raise HTTPException(status_code=404, detail="Todo not found")

@todo_router.post("/todos")
async def create_todo(todo: TodoItem  = Body(..., title="The todo item to create")) -> dict:
    todos.append(todo)
    return {"todo": todo}

@todo_router.put("/todos/{todo_id}")
async def update_todo(todos: UpdateTodoItem ,todo_id: int = Path(..., title="The ID of the todo item to update"), todo: UpdateTodoItem = Body(..., title="The todo item to update")) -> dict:
    print(todos)
    todo = [todo for todo in todos if todo["id"] == todo_id]
    if todo:
        todo[0]["title"] = todo["title"]
        todo[0]["description"] = todo["description"]
        todo[0]["completed"] = todo["completed"]
        return {"todo": todo}
    raise HTTPException(status_code=404, detail="Todo not found")
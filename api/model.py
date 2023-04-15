from pydantic import BaseModel
from typing import List


class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True
        Schema_extra = {
            "example": {
                "id": 1,
                "title": "Buy milk",
                "description": "Buy 2L of milk",
                "completed": False
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        orm_mode = True
        Schema_extra = {
            "example": {
                "todos": [
                    {
                        "id": 1,
                        "title": "Buy milk",
                        "description": "Buy 2L of milk",
                        "completed": False
                    },
                    {
                        "id": 2,
                        "title": "Buy eggs",
                        "description": "Buy 12 eggs",
                        "completed": False
                    }
                ]
            }
        }


class UpdateTodoItem(BaseModel):
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True
        Schema_extra = {
            "example": {
                "title": "Buy milk",
                "description": "Buy 2L of milk",
                "completed": False
            }
        }


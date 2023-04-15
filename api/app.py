from fastapi import FastAPI, APIRouter
from todo import todo_router

app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return {"Hello": "World"}

app.include_router(todo_router)
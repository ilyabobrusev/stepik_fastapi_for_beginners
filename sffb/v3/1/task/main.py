from fastapi import FastAPI, status, Body

app = FastAPI()


todo_db = {0: "The first note"}


@app.get("/todos")
async def get_all_messages() -> dict:
    return todo_db


@app.get("/todos/{todo_id}")
async def get_message(todo_id: int) -> str:
    return todo_db[todo_id]

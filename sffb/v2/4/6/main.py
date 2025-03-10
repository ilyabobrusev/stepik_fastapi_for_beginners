from fastapi import FastAPI

app = FastAPI()


@app.get("/user")
async def login(username: str, age: int = 30) -> dict:
    return {"user": username, "age": age}


@app.get("/user_none")
async def login_none_(username: str, age: int | None = None) -> dict:
    return {"user": username, "age": age}

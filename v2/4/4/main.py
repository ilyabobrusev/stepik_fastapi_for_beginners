from fastapi import FastAPI

app = FastAPI()


@app.get("/user")
async def login(username: str, age: int) -> dict:
    return {"user": username, "age": age}

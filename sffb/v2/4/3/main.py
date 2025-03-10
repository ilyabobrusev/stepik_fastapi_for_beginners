from fastapi import FastAPI

app = FastAPI()


@app.get("/user/profile")
async def profile() -> dict:
    return {"profile": "View profile user"}


@app.get("/user/{user_name}")
async def user(user_name: str) -> dict:
    return {"user": user_name}

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


@app.get("/hello/{user}")
async def welcome_user(user: str) -> dict:
    return {"user": f'Hello {user}'}

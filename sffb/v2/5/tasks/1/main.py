from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/user/{name}")
async def user(
        name: Annotated[
            str, Path(min_length=4, max_length=20, description='Enter your name')])-> dict:
    return {"user_name": name}

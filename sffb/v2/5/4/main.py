from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/user")
async def search(
        people: Annotated[
            list[str], Query()] = "Default") -> dict:
    return {"user": people}

from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/category/{category_id}/products")
async def category(
        category_id: Annotated[
            int, Path(gt=0, description='Category ID')],
        page: int)-> dict:
    return {"category_id": category_id, "page": page}

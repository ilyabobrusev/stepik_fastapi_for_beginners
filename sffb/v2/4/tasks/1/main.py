from fastapi import FastAPI

app = FastAPI()


@app.get("/product/{product_id}")
async def detail_view(product_id: int) -> dict:
    return {"product": f'Stock number {product_id}'}

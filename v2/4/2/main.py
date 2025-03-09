from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


@app.get("/hello/{first_name}/{last_name}")
async def welcome_user(first_name: str, last_name: str) -> dict:
    return {"user": f'Hello {first_name} {last_name}'}

@app.get("/order/{order_id}")
async def order(order_id: int) -> dict:
    return {"id": order_id}

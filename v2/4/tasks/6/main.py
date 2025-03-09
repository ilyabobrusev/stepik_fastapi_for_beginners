from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def users(name: str = 'Undefined', age: int = 18) -> dict:
    return {'user_name': name, 'user_age': age}

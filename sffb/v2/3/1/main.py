from fastapi import FastAPI

app = FastAPI(
    docs_url=None,  # Disable docs (Swagger UI)
    redoc_url=None,  # Disable redoc
    openapi_url=None,  # Disable openapi.json
)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

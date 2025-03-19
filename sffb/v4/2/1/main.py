from fastapi import FastAPI, Depends, Query, HTTPException

app = FastAPI()


async def pagination_path_func(page: int):
    if page < 0:
        raise HTTPException(status_code=404, detail="Page does not exist")
    if page == 0:
        raise HTTPException(status_code=400, detail="Invalid page value")


async def pagination_func(limit: int = Query(10, ge=0), page: int = 1):
    return {'limit': limit, 'page': page}


@app.get("/messages", dependencies=[Depends(pagination_path_func)])
async def all_message(pagination: dict = Depends(pagination_func)):
    return {"messages": pagination}


@app.get("/comments")
async def all_comments(pagination: list = Depends(pagination_func)):
    return {"comments": pagination}
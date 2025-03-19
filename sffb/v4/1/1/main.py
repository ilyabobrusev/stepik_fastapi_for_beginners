from fastapi import FastAPI, Depends, Query

app = FastAPI()


# @app.get("/messages")
# async def all_messages(limit: int = 10, page: int = 1):
#     return {"messages": [{'limit': limit, 'page': page}]}


# @app.get("/comments")
# async def all_comments(limit: int = 10, page: int = 1):
#     return {"comments": [{'limit': limit, 'page': page}]}


async def pagination_func(limit: int = Query(10, ge=0), page: int = 1):
    return [{'limit': limit, 'page': page}]


@app.get("/messages")
async def all_messages(pagination: list = Depends(pagination_func)):
    return {"messages": pagination}


@app.get("/comments")
async def all_comments(pagination: list = Depends(pagination_func)):
    return {"comments": pagination}

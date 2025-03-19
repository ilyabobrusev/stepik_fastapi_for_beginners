from fastapi import FastAPI, Depends
from starlette.requests import Request


app = FastAPI()


class Paginator:
    def __init__(self):
        self.limit = 10
        self.page = 1

    def __call__(self, limit: int):
        if limit < self.limit:
            return [{'limit': self.limit, 'page': self.page}]
        else:
            return [{'limit': limit, 'page': self.page}]


my_paginator = Paginator()


@app.get("/users")
async def all_users(pagination: list = Depends(my_paginator)):
    return {"user": pagination}


async def sub_dependency(request: Request) -> str:
    return request.method


async def main_dependency(sub_dependency_value: str = Depends(sub_dependency)) -> str:
    return sub_dependency_value


@app.get("/test/")
async def test_endpoint(test: str = Depends(main_dependency)):
    return test

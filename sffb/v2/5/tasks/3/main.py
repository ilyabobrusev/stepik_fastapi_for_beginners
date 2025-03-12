from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

profiles_dict = {
    'alex': {'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'},
}

@app.get("/users")
async def retrieve_user_profile(
        username: Annotated[str, Query(min_length=2, max_length=50, description='Имя пользователя')])-> dict:
    return profiles_dict.get(username, {'message': f'Пользователь {username} не найден.'})

## if use withoud profiles_dict.get
#    if username in profiles_dict:
#        return profiles_dict[username]
#    else:
#        return {"message": f"Пользователь {username} не найден."}

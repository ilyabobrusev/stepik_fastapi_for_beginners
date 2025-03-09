from fastapi import FastAPI

app = FastAPI()

country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
}

@app.get('/country/{country}')
async def list_cities(country: str, limit:int):
    return {'country': country, 'cities': country_dict[country][: limit]}


# from fastapi import FastAPI

# app = FastAPI()

# # Пример словаря country_dict
# country_dict = {
#     'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
#     'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
# }

# @app.get("/country/{country}")
# async def list_cities(country: str, limit: int):
#     # Получаем список городов для указанной страны
#     cities = country_dict.get(country, [])
    
#     # Ограничиваем количество городов в списке
#     limited_cities = cities[:limit]
    
#     # Возвращаем ответ в виде словаря
#     return {
#         "country": country,
#         "cities": limited_cities
#     }

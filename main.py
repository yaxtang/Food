from fastapi import FastAPI
from request import getfood
import requests

app = FastAPI()

# Set up api return and set function in request 

@app.get("/")
def root():
    response = getfood()
    return response
    # print(response)
    # return {"response":response}
    # return {'message': 'Welcome to GeeksforGeeks!'}

@app.get('/recipt={name}')
def first_user(name:str):
    api_url = "https://www.themealdb.com/api/json/v1/1/search.php?s="+name
    all_users = requests.get(api_url).json()
    print(all_users)
    # user1 = all_users[0]
    name = all_users["meals"]
    # email = user1["idMeal"]
    return {'Mealname': name}

@app.get("/random")
def random():
    api_url = "https://www.themealdb.com/api/json/v1/1/random.php"
    randomRecipt = requests.get(api_url).json()
    print(randomRecipt)
    return randomRecipt
    # api_url = ""

@app.get('/ingredient={name}')
def main_ingredients(name:str):
    api_url = "https://www.themealdb.com/api/json/v1/1/filter.php?i="+name
    mainIngredients = requests.get(api_url).json()
    print(mainIngredients)
    return mainIngredients


# @app.get("/")
# async def root():
#     # if (name == "abc"):
#     url = "http://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata"

#     response = requests.get(url)
#     return response
    
#     # return {"message": "Hello World"}

# # search name of the recipts
# async def call_api(url: str):
#     url = "http://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata"
#     response = await requests.get(url)
#     return response.json()

# @app.get("/foodname={name}")
# async def root(name: str):
    
#     response = await call_api("a")
#     if response.status_code == 200:
#         print(json.loads(test_get_response.content.decode('utf-8')))
#     a = response.json()
#     print(response.json())
#     return a
#     # if (name == "abc"):
#     #     url = "http://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata"

#     #     response = requests.get(url)
#     #     return response
#     # return {"message": name}
    


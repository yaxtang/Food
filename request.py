import requests


def getfood():
    api_url = "https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata"
    all_users = requests.get(api_url).json()
    print(all_users)
    # user1 = all_users[0]
    name = all_users["meals"]
    # email = user1["idMeal"]
    return {'Mealname': name}
    # return response


def randomRecipt():
    
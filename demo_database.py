import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="13265616108",
  database="food_recipes"
)
mycursor = mydb.cursor(buffered=True)
# mycursor = mydb.cursor()
# create a database to store food recipes and a table recipe, only excute at the first time
# mycursor.execute("CREATE DATABASE food_recipes")
# mycursor.execute("CREATE TABLE recipe (MEAL varchar(255), MAIN_INGREDIENT varchar(255), RATE INT)")

# mycursor.execute("USE food_recipes;") # will show "Database changed"
# mycursor.execute("Show tables;") # should only show a table recipe
# mycursor.execute("INSERT INTO recipe (MEAL, MAIN_INGREDIENT, RATE) VALUES ('Strawberry Cheese Mousse','Strawberry, Milk, Cream Cheese','5')")

sql = "INSERT INTO recipe (MEAL, MAIN_INGREDIENT, RATE) VALUES (%s, %s, %s)"
val = [
  ("cabbage soup", "cabbage", 4),
  ("carrots soup", "cabbage,carrotes, onions, bacon", 4)
       ]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM recipe") # should only show a table recipe

for x in mycursor:
  print(x)
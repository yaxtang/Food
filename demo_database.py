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
mycursor.execute("USE food_recipes;") # will show "Database changed"
# mycursor.execute("SHOW tables;")
# mycursor.execute("""ALTER TABLE meal_recipes (
#                   MealId int NOT NULL AUTO_INCREMENT(1),
#                   MealName varchar(255) NOT NULL,
#                   MainIngredient varchar(255),
#                   RATE int, 
#                   PRIMARY KEY (MealId))""")
# mycursor.execute("ALTER TABLE meal_recipes AUTO_INCREMENT=0")
# mycursor.execute("CREATE DATABASE food_recipes")
# mycursor.execute("DROP TABLE recipe;")
# mycursor.execute("ALTER TABLE recipe ADD CONSTRAINT PRIMARY KEY (MEALID);")
# mycursor.execute("show tables;")
# mycursor.execute("describe meal_recipes;") # should only show a table recipe
# mycursor.execute("""INSERT INTO meal_recipes (MealName, MainIngredient, Rate) VALUES ('Strawberry Cheese Mousse','Strawberry, Milk, Cream Cheese','5')""")

# sql = "INSERT INTO recipe (MEAL, MAIN_INGREDIENT, RATE) VALUES (%s, %s, %s)"
# val = [
#   ("cabbage soup", "cabbage", 4),
#   ("carrots soup", "cabbage,carrotes, onions, bacon", 4)
#        ]
# mycursor.executemany(sql, val)
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
# mycursor.execute("SELECT * FROM meal_recipes") # should only show a table recipe

# for x in mycursor:
#   print(x)


##########
# function: addMeal 
# add a meal to the database
##########
def addMeal(mealName:str, MainIngredient:str, Rate:int):
  mycursor.execute("""INSERT INTO meal_recipes (MealName, MainIngredient, Rate) 
                   VALUES ('Mousse','Milk, Cream Cheese','5')""")
  mycursor.execute("""INSERT INTO meal_recipes (MealName, MainIngredient, Rate) 
                   VALUES ('Tikka Masala','Chicken, Chicken, Milk, Cream Cheese','1')""")

  mycursor.execute("SELECT * FROM meal_recipes") # should only show a table recipe
  # need to commit to confirm the change to record
  mydb.commit()

  for x in mycursor:
    print(x)

addMeal('a','a',1)
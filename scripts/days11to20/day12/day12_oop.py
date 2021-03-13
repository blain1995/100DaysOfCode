# from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepSkyBlue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("pokemon_name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column('type', ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)

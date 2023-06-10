#day04ofpython

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ra = len(names)-1

a = random.randint(0,ra)

print(f"{names[a]} is going to buy the meal today!")

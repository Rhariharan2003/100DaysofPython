#days030fpython

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

amt = 0

if size == 'S':
    amt += 15
elif size == 'M':
    amt += 20
elif size == 'L':
    amt += 25
if add_pepperoni == 'Y' and size == 'S':
    amt += 2
elif add_pepperoni == 'Y' and (size == 'M' or size == 'L') :
    amt += 3
if extra_cheese == 'Y':
    amt += 1
print("Your final bill is: $",amt)

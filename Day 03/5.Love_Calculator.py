#days03ofpython

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
count1= 0
count2= 0
count1 = count1 + name1.count('t')

count1 = count1 +  name1.count('u')

count1 = count1 +  name1.count('r')

count1 = count1 +  name1.count('e')

count1 = count1 + name2.count('t')

count1 = count1 +  name2.count('u')

count1 = count1 +  name2.count('r')

count1 = count1 +  name2.count('e')


count2 = count2 + name1.count('l')

count2 = count2 +  name1.count('o')

count2 = count2 +  name1.count('v')

count2 = count2 +  name1.count('e')

count2 = count2 + name2.count('l')

count2 = count2 +  name2.count('o')

count2 = count2 +  name2.count('v')

count2 = count2 +  name2.count('e')

tot = str(count1) + str(count2)
tot = int(tot)

if(tot < 10 or tot > 90):
    print(f"Your score is {tot}, you go together like coke and mentos.")
elif (tot >= 40 and tot <= 50):
    print(f"Your score is {tot}, you are alright together.")
else:
    print(f"Your score is {tot}.")

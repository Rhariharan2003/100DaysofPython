#day08ofpython

#Write your code below this line 👇

def prime_checker(number):
 g = 2
 for i in range(2,number+1):
   if( number %  i == 0) and ( number != i ):
     g = g + 1
   
 if g == 2:
    print("It's a prime number.")
 else:
    print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

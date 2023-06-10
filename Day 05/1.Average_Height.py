#day05ofpython

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split( )
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
ans = 0
l = 0
for i in   student_heights:
 ans = ans + i
 l+=1
print(round(ans/l))


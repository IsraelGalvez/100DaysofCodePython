# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
plus_heights = 0

for heights in student_heights:
    plus_heights += heights
    count += 1

average_height = round(plus_heights/count)

print(average_height)
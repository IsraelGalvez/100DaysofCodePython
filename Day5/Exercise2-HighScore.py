# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
student_higher_score = 0

for student in student_scores:
    if student > student_higher_score:
        student_higher_score = student

print(f"The highest score in the class is: {student_higher_score}")
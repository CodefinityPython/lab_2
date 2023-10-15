scores = []

students_number = int(input("Введіть кількість студентів Вашої групи:"))

for i in range(students_number):
    score = int(input(f"Введіть бал Вашого студента {i+1}: "))
    scores.append(score)

scoresSum = sum(scores)
avScore = scoresSum / students_number

print("Середній бал Вашої групи:", avScore) 
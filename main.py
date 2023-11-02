# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
students_num = int(input("Enter the number of students:"))

# Зчитування балів студентів та додавання їх до списку
for num in range(students_num):
    scores.append(int(input("Enter the students' score:")))

# Обчислення суми балів
score_sum = 0
for score in scores:
    score_sum += score

# Обчислення середнього балу
av_score = round(score_sum/students_num, 1)

# Виведення результату на екран
print (f"The average score is {av_score}")

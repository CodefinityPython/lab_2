# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
num_students = int(input("Введіть кількість студентів у групі: "))
print(num_students)
# Зчитування балів студентів та додавання їх до списку
for i in range(num_students):
    score = float(input(f"Введіть бал для студента {i + 1}: "))
    scores.append(score)

# Обчислення суми балів
total_score = sum(scores)

# Обчислення середнього балу
average_score = total_score / num_students

# Виведення результату на екран
print(f"Середній бал для групи студентів: {average_score}")

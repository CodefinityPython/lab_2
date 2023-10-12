# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
students_count = int(input("Please enter the amount of students: "))

# Зчитування балів студентів та додавання їх до списку
for counter in range(students_count):
    scores.append(int(input("Please enter students score: ")))

# Обчислення суми балів
score_sum = 0
for score in scores:
    score_sum += score

# Обчислення середнього балу
avg_score = score_sum / students_count

# Виведення результату на екран
print(avg_score)

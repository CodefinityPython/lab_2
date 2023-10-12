# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
student_count = int(input("Введіть кількість студентів:"))

# Зчитування балів студентів та додавання їх до списку
for i in range(student_count):
    currentScore = int(input(f"Введіть бал студента {i+1}:"))
    scores.append(currentScore)

# Обчислення суми балів
totalSum = sum(scores)

# Обчислення середнього балу
avarageScore = totalSum / student_count

# Виведення результату на екран
print("Середній балл студентів:", avarageScore)

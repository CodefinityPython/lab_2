# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
print("Enter the number of students")
number = int(input())


# Зчитування балів студентів та додавання їх до списку
for i in range(number):
    score = float(input(f"Enter the score for the student {i + 1}: "))
    scores.append(score)

# Обчислення суми балів
totalsum = sum(scores)

# Обчислення середнього балу
avarage_score = totalsum / number

# Виведення результату на екран
print("Students' grade point average:", avarage_score)
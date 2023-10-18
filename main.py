# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
amount_of_students = int(input('Введіть кількість студентів: '))

# Зчитування балів студентів та додавання їх до списку
for i in range(amount_of_students):
    scores.append(int(input('Введіть оцінку')))


# Обчислення суми балів
sum_scores = sum(scores)

# Обчислення середнього балу
average_score = sum_scores/amount_of_students

# Виведення результату на екран
print(f'Середній бал: {average_score}, всього {amount_of_students}, студента(ів)')

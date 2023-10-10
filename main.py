# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
num_students =int(input("Enter the number of students in the group: "))

# Зчитування балів студентів та додавання їх до списку
for i in range(num_students):
    score = float(input(f"Enter the score for a student {i+1}: "))
    scores.append(score)

# Обчислення суми балів
total_score = sum(scores)

# Обчислення середнього балу
average_score = total_score / num_students

# Виведення результату на екран
print(f"Average score for a group of students: {average_score}")

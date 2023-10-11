# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
kilkist_studentiv = int(input("Будь ласка, введіть кількість студентів у групі: "))



# Зчитування балів студентів та додавання їх до списку
for student in range(kilkist_studentiv):
 score = int(input("Введіть бал Вашого студента: ")) 
scores.append(score)
# Обчислення суми балів
scores_sum = 0
for score in scores:  
    scores_sum += score

# Обчислення середнього балу


# Виведення результату на екран
score_average = scores_sum / kilkist_studentiv
print("Середній бал Вашої групи:", score_average)


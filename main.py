
list_of_scores = []

# Запит користувача на введення кількості студентів у групі

list_of_students = int(input('Please, enter the number of students: '))


for students in range(list_of_students):
    score = int(input('Enter your score: '))
    list_of_scores.append(score)

# Обчислення суми балів
scores_sum = 0
for score in list_of_scores: 
    scores_sum += score

# Обчислення середнього балу
medium_score = scores_sum/list_of_students
# Виведення результату на екран
print(medium_score)
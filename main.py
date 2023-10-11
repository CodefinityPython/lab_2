# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
students = int( input('Кількість студентів:') )

# Зчитування балів студентів та додавання їх до списку
for i in range(students) :
    ball = float(input('Бал студента:'))   
    scores.append(ball) 
# Обчислення суми балів
ball_sum = sum(scores)

# Обчислення середнього балу
#ball_ser = str( ball_sum / students)
ball_ser = ball_sum / students

# Виведення результату на екран
#print(f'Середній бал студентів:{ball_ser} ')
#print('Середній бал студентів:' + ball_ser ) 
print('Середній бал студентів:', ball_ser )
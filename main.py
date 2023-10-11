# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
scores = []

# Запит користувача на введення кількості студентів у групі
try:
    studentsCount = int(input("Введіть кількість студентів: "))
except:
   print("Не корректне значення")
   exit()

# Зчитування балів студентів та додавання їх до списку

for i in range(studentsCount):
    try:
       currentScore = int(input(f"Введіть оцінку студента {i+1}: "))
       scores.append(currentScore)
    except:
      print("Не корректне значення")
      exit()

# Обчислення суми балів

totalScoreSum = sum(scores)

# Обчислення середнього балу

averageScore = totalScoreSum / studentsCount

# Виведення результату на екранф

print(f"Cередній бал: {averageScore}")
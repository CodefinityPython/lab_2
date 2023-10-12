# Це файл для твого роз'язку


# Створення порожнього списку для балів студентів
students_list = []

# Запит користувача на введення кількості студентів у групі
n = int(input("Enter number of students: "))

# Зчитування балів студентів та додавання їх до списку
for i in range(n):
    student_mark = int(input(f"Enter the mark for student {i+1}: "))
    students_list.append(student_mark)

# Обчислення суми балів
counter = 0

for i in range(len(students_list)):
    counter += students_list[i]

# Обчислення середнього балу
average_value = counter / n 

# Виведення результату на екран
print("----------------------------------")
print("Average value = ", average_value)

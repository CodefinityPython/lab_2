scores = []

num = int(input('Введіть кількість студентів '))
for i in range(num):
    scores.append(int(input('Введіть кількість балів ')))
print(sum(scores) / num)
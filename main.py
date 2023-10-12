scores = []

numst = int(input('Введіть кількість студентів:'))

for i in range(numst):
    sctd = int(input('Введіть бал студента:'))
    scores.append(sctd)

scsm = 0
for sctd in scores:
    scsm += sctd

score_average = scsm / numst

print("Середній бал Вашої групи:", score_average)


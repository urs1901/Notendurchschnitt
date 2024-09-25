grades = []
count = int(input("Wie viele Noten möchtest du eingeben? "))
for i in range(1, count+1):
    grade = int(input("Nenne deine "+str(i)+". Note "))
    grades.append(grade)
average = sum(grades) / count
print("Dein Notendurchschnitt ist "+str(average))

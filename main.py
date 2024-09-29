def gradeAverage():
    grades = []
    count = int(input("Wie viele Noten möchtest du eingeben? "))
    for i in range(1, count+1):
        grade = int(input("Nenne deine "+str(i)+". Note "))
        if grade in range(1,7):
            grades.append(grade)
        else:
            print("Nur Zahlen zwischen 1 und 6 sind zulässig")
            exit()
    average = sum(grades) / count
    print("Dein Notendurchschnitt ist "+str(average))

if __name__ == "__main__":
    gradeAverage()
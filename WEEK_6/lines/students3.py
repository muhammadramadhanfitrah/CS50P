import csv


name = input("What's your name? ")
home = input("Where's yout home? ")


with open("students3.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})


students = []


with open("students3.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)


for student in students:
    print(f"{student['name']} is from {student['home']}")

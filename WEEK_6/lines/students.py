with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        name = row[0]
        address = row[1]

        print(f"{name} is in{address}")

        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


students = []


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students, key=len):
    print(student)


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

print(students)


for student in sorted(students[0][0]):
    print(f"{student['name']} is in {student['house']}")


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]


def get_house(student):
    return student["house"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


for student in sorted(students, key=lambda student: len(student["name"])):
    print(f"{student['name']} is in {student['house']}")

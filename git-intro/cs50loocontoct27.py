students={
    "Hermione":"Griffyndor",
    "Harry":"Griffyndor",
    "Ron":"Griffyndor",
    "Draco":"Slytherin",
}

for  student in students:
    print(student,students[student],sep=", ")


students =[
    {"name":"Hermione","house":"Griffyndor","patronus":"otter"},
    {"name":"Harry","house":"Griffyndor","patronus":"stag"},
    {"name":"Ron","house":"Griffyndor","patronus":"jack russellt erier"},
    {"name":"Draco","house":"Slytherin","patronus":"otter"},
]
for student in students:
    print(student["name"],student["house"],student["patronus"],sep=", ")
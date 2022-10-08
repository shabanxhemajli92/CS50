student={"name":"John",
"age":25,
"courses":["Math","Compsci"]}
student["phone"]="555-555"
student["name"]="jane"
# print(student)

student.update({"name":"Jane","age":26,"phone":"333-333"})
# print(student)
age=student.pop("age")
print(age)

# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())
for key,value in student.items():
    print(key,value)
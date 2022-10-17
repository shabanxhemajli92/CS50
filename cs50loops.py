i=1
while i < 3:
     print("meow")
     i += 1

for i in [0,1,2]:
    print("meow")


for _ in range(1000000):
     print("meow")

students=["harmonie","harry","ron"]


def student_loop(list):
    for n in list:
        # if n in list:
        return " ".join(list)


print(student_loop(students))


for n in range(len(students)):
    print(n + 1, students[n])

""""Dictionaries"""
students = ["harmonie", "harry", "ron", "draco"]
houses = ["Griffyndor", "grifyndor", "skyrad", "johnsonville"]

s_dict = dict(zip(students, houses))
print(s_dict)


def zipped(list1, list2):

    new_dict = dict(zip(list1, list2))
    return new_dict


print(zipped(students, houses))
print(type(zipped(students, houses)))

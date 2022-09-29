# name = ('Mirjam', 'Lingoda','english','good student')
# other_name = ('Peer', 'Hofman','class representative')

# # tuples (are immutable)

# name = name + other_name
# name=other_name
# other_name = name + other_name
# print(other_name)
# # print(name)

# numbers = (1,2,3,4,5,6,7,8,9)
# num = (1,2,3,4,5)
# #print(numbers[0:1]) # 2, 3, 4, 5
# print(numbers[2:6])
# print(numbers[6])
# print(numbers[-3])
# print(len(num))
# inbuilt "len" function/method
#print(len(numbers))
#print(numbers[0])

# negative indexing
#print(numbers[-2])

# def greeting_fullname(first_name, last_name, gender):
#     greeting = ''
#     full_name = f'{first_name} {last_name}'
#     if gender == 'male':
#         greeting = f"Good morning Mr. {first_name}"
#     else:
#         greeting = f"Good morning Ms. {first_name}"
#     return (greeting, full_name)

# def greeting_fullname(first_name, last_name, gender="Mr./Ms."):
#     full_name = f'{first_name} {last_name}'
#     greeting = ''
#     if gender == 'male':
#         greeting = f"Good morning Mr. {first_name}"
#     elif gender == 'female':
#         greeting = f"Good morning Ms. {first_name}"
#     else:
#         greeting = f"Good morning {gender} {first_name}"
#     return (greeting, full_name)
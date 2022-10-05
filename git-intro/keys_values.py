# fruit_colors = {
#     "apple": "red",
#     "berries": "blue"
# }

# for color in fruit_colors:
#     print(color)#prints keys

# for items in fruit_colors.items():
#     print(items)#prints items

# for values in fruit_colors.values():
#     print(values)#print values

# k={
#     "soccer":"played with a ball",
#     "paddle":"fake tenis",
#     "poker":"played in vegas",
# }


# if k.fromkeys("er"):
#     k.pop("soccer")
#     k.pop("poker")
   
#     print(k)        



#weekday=["monday","tuesday","wednesday","thursday","friday"]

# for index, days in enumerate(weekday,start=0):
#     print(f"{days.capitalize()} is day {index}")


# max_val=0
# numbers=[3,4,1,2,100,5,6]
# for n in numbers:
#     if n > max_val:
#         max_val=n
# print(max_val)#prints 100
# max_valu=max(numbers)
# print(max_valu)#also prints 100
from unicodedata import name


books = [
    {"cost": 10, "name": 'Python 2'},
    {"cost": 1, "name": 'Best tourism sites in Napoli'},
    {"cost": 5, "name": 'Basket Weaving for Pros'},
    {"cost": 8, "name": 'Java for dummies'},
]
# print(sorted(books, key=lambda book: book['cost']))

# readable!
# func = lambda book: book['cost']
# print(sorted(books, key=func))
#func = lambda book: book['name']
#print(sorted(books, key=func))
#print(sorted(books, key=lambda book: book['name']))
print(sorted(books, key=lambda book: book['name'],reverse=True))
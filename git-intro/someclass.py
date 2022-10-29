class Person:
    def __init__(self,age,weight,height,first_name,last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

    def walking(self):
        print(f"{self.first_name} is walking")
    def destination(self):
        print(f"{self.first_name} is going to Sao Paolo")    
user = Person(21,80,176,"John","Johnson")
print(user.destination())        
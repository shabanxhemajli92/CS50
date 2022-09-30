import time

name = {"first_name":"John",
    "last_name":"Doe"}#initial value
time.sleep(1)
   
print(name)
# "Pass by reference" variables can change
def full_name(name):
    name["first_name"]="Alice" 
    name["last_name"] = "Hoffmann"#assigment of the value
    return name
time.sleep(1)
full_name(name)#this is the change in the value of the variable
print(name)


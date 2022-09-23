# names=["John","Jim","Alvin"]
# for name in names:
#     print(name)

def full_name(*args):
    
    full_string = ""
    for name in args:
        full_string += f"{name} " 
    return full_string


print(full_name("Felipe", "Gonzales", "Garcia", "Gonzales", "Garcia", "Gonzales", "Garcia", "Gonzales", "Garcia", "Gonzales", "Garcia", "Gonzales", "Garcia", "Gonzales", "Garcia"))
print(full_name("Gonzales", "Garcia"))
print(full_name("Gonzales")) 

  
    




     
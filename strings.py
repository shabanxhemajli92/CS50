

#ask the user for their name and strip the white spaces and capitalize
name = input("Whats your name?").strip().title()

#split users name into first name and last name
first, last = name.split(" ")


#say hello to user
print(f"Hello,{first}")




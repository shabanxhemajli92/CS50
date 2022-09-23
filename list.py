from operator import index


names = ["Victor", "Peter", "Mary","Emily","Kirk", "John", "Badara", "Peer"]
# 
# using an index, replace "Peer" with "Malcom X"

# Add two names to the list of names

# Experiment with the methods in a list using dir(names)

#Task 1
index_of=names.index("Peer")
names[index_of]="Malcom X"
names.append("Kirk")
names.append("Leo Messi")
names.insert(3,"John")
print(names)
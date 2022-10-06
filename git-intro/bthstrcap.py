
names = ['jacque doe', 'peer doe', 'mirjam doe', 'shaban doe']
new_lst=[]
for name in names:
    new_lst.append(name.title())
print(new_lst)

all_names_capitalize = map(lambda name: name.title(), names)
print(list(all_names_capitalize))
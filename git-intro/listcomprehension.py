# my_list=[1,2,3]
# double=[element *2 for element in my_list]
# print(double)


# users=[{'name':'manuel','age':31},{'name':'john','age':30},{'name':'abel','age':37}]
# user_name=[user['name']for user in users if user['age'] > 30 and user['name']=='abel']
# print(user_name)
# user_age=[user['age']for user in users]
# print(user_age)

user_groups = [
    [
        {'name':'Manuel','age':31},
        {'name':'Max','age':30},  
    ],

    [
        {'name':'Sarah','age':29},
        {'name':'Julie','age':32}
    ]   
]
user_name=[person['name'] for group in user_groups for person in group if person['age'] > 30]
print(user_name)

#list comprehension in function form
def list_comp(lst):
    new_lst=[]
    for keys in lst:
        new_lst.append(keys)
        for values in lst:
            new_lst.append(values)
print(list_comp(user_groups))
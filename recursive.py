import sys
import resource

sys.getrecursionlimit()
# print(sys.getrecursionlimit())

# def test(n):
#    if n==1:
#     print("finish")
#     return test(n-1) 

list_=[3,4,5,6]

# def get_sum(list):
#     total = 0
#     for i in list:
#         total += i
#     return total 
# print(get_sum(list_))  

# def rec_funlst(n,list):
#     n = int
#     if n in list:
#         return sum(rec_funlst(list),start=n)
#     else: 
#         return 0
# print(rec_funlst(5,list_))         

def get_Sum(list):
    if not list:
        return 0  # End of recursion
    else:
        return list[0] + get_Sum(list[1:])
print(get_Sum(list_))      
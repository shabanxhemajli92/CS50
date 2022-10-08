# score=int(input("Score: "))

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")  
# elif score >= 70:
#     print("C") 
# elif  score >= 60:
#     print("D")
# else:
#     print("F")  
 
def main():
    x = int(input("whats x?"))
    if is_even(x):
        print("Even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False    
main()
from curses import COLOR_MAGENTA
import os
import time
import colorama as cl
cl.init()

y=int(input(cl.Fore.GREEN+"Whats the first number?"+cl.Fore.RESET))
x=int(input(cl.Fore.CYAN+"whats the second number?"+cl.Fore.RESET))

time.sleep(1)
os.system("clear")
def add(n,n1):
    sum=n+n1
    print("the addition of the first and second number is:",sum)
    return sum

time.sleep(1)
os.system("clear")   
add(x,y)
def substraction(n,n1):
    sum=n-n1
    print("the substraction of the first and second number is:",str(sum))
    return(sum)
substraction(x,y)

time.sleep(1)
os.system("clear")
def multiplication(n,n1):
    sum=n*n1
    print("the multiplication of the first and second number is:",sum)
    return(sum)
multiplication(x,y)

time.sleep(1)
os.system("clear")
def division(n,n1):
    sum=n//n1
    print("the division of the first and second number is:",sum)
    return(sum)
division(x,y)        

import time
inp_var=0
while inp_var <= 100:
    inp_var=int(input("enter your age: "))
    time.sleep(1)
    if inp_var==10:
        print("go to bed at 10")
        break
    elif inp_var>=10 and inp_var <=18:
        print("you can still play with your friends")
        break 
       
    elif inp_var==18:
        print("stay as long as you want")
        break
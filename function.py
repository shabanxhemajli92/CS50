from unicodedata import name


def main():
    name=input("what is your name?")
    hello()

def hello():
    print("hello,",name)    

main()


def make_title(func): # we expect the function to return a string
    def inner(name):
        return name,func().title()

    return inner        

@make_title
def greetings():
    return "mr"

print(greetings("fausto doe"))
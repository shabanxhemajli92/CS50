

def make_title(func): # we expect the function to return a string
    def inner(name):
        return name,func().title()

    return inner        

@make_title
def greetings():
    return "mr"

print(greetings("fausto doe"))

names = ['peter doe', 'peer doe', 'mary doe', 'tom doe', 'john doe']

capital_names=[n.title() for n in names]
print(capital_names)
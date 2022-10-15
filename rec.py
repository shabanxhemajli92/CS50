def mul(n):
    if n<=1:
        return 1

    
    return n * mul(n-1)

print(mul(4))

def add(n):
    if n <1:
        return 1
    return n + add(n-1) 

print(add(5))      


def inc(n):
    if n > 1000:
        return 1000
    return n + inc(n*5)
print(inc(3))
30+30*5

for n in range(3,1000):
    calc_var=n+n*5
  
    if calc_var == 1468:
        break
print(calc_var)

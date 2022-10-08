# a=[3,10,-1]
# a.append(1)
# a.append("hello")
# a.pop()
# a[0]=100
b=["banana","apple","microsoft"]
temp=b[0]
b[0]=b[2]
b[2]=temp
print(b)
b[1],b[0]=b[0],b[1]
print(b)
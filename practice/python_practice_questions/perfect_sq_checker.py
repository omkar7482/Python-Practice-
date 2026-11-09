a = int(input())
b = 0 
c = 0 
if a >= 0 :
    b = a ** (1/2)
    c = int(b)
if c * c == a :
    print("perfect sq : ")
else:
    print(-1)
print(b)
print(c)
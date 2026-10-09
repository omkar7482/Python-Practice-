num = int(input())
a = 1 
while (num > a):
    b = 1
    for i in range(a,num + 1):
        b = b * i 
    break

print(b)

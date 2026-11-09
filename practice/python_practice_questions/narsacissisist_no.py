def narcissistic( value ):
    a = value
    b = str(a)
    c =[]
    d = len(b)
    e = 0
    for i in b :
        c.append(i)
    for i in c :
        e += (int(i) ** d)
    if a == e :
        return True
    else:
        return False
    


a = narcissistic(153)
print(a)




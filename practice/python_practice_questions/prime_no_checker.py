def prime_no_checker(a):    
    b = a // 2
    c = 0
    if 3 >= a >1 :
        print("Prime No")
    elif a > 3 :
        for i in range(b,1,-1):
            if a % i == 0 :
                c += 1
        if c == 0:
            print("Prime No")
        else:
            print("Not Prime NO ")
    else:
        print("Invalid Input")


c =  15
prime_no_checker(123457)

import sys
sys.set_int_max_str_digits(1000000000)

a = int(input())
if a < 0 :
    print("Not defined")
else:
    b = 1 
    c = 1 
    while a >= b :
        c = b * c 
        b = b + 1 
    print(c)
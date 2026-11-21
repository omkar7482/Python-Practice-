a = int(input())
def print_hollow_triangle(n):
    for i in range(n+1):
        if n > i > 2:
            print("*" + (i-2)* " "+"*")
        else :
            print("*" * i)

print_hollow_triangle(a)

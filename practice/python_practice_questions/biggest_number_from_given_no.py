def descending_order(num):
    # Bust a move right here
    if num == "None":
        return 0
    else:
        a = str(num)
        b = []
        for char in a :
            b.append(char)
        c = "".join(sorted(b , reverse=True))
        return int(c)

a = input("Type here : ")

print(descending_order(a))







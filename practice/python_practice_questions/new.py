l = [0, -1, None, -3]
# l = [1, -2, 3, 0, None, 4]
a = []
for i in l:
    if isinstance(i, (int, float)) and i > 0:
        a.append(i)
    
print(len(a))

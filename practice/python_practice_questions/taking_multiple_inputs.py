n = int(input().strip())
lines = []
for _ in range(n):
    lines.append(input().strip())

for line in lines:
    result = []
    for char in line.lower():
        if char in 'aeiou':
            result.append(char.upper())
        else:
            result.append(char)
    print(''.join(result))
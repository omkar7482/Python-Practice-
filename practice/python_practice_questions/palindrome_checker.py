def check_palindrome(a):
    a = str(a)
    if a[::-1] == a[0::]:
        return "palindrome"
    else:
        return "Not palindrome"
    return check_palindrome

a =input()
print(check_palindrome(a))

def vowel_counte_to_end_of_every_word(a):
    list_of_word = a.split(" ")
    vowels = "AEIOUaeiou"
    list_of_vowel_counted = []
    count = 0 

    for word in list_of_word:
        count = 0
        for i in word:
            if i in vowels:
                count += 1 
        list_of_vowel_counted.append(f"{word}({count})")
    return " ".join(list_of_vowel_counted)



a = input("Enter your text here: ")
print(vowel_counte_to_end_of_every_word(a))

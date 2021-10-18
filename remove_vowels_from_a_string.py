vowels = ('a', 'e', 'i', 'o', 'u')

mes = input("enter text = ")

new_mes = ""

for letter in mes:
    if letter not in vowels:
        new_mes += letter

    if letter in vowels:
        print(letter, "is a vowel.")

print(new_mes)

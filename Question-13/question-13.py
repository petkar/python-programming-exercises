sentence = input("Enter a sentence: ")
digits, letters = 0, 0
for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isnumeric():
        digits += 1
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")

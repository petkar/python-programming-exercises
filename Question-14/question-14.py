sentence = input("Enter a sentence: ")
upper_count = 0
lower_count = 0
for char in sentence:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print(f"UPPER CASE {upper_count}")
print(f"LOWER CASE {lower_count}")

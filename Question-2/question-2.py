num = int(input("Enter a positve integer: "))
if num < 0:
    print("Try again with a positive integer.")
fact = 1
while num > 0:
    fact *= num
    num -= 1
print(fact)

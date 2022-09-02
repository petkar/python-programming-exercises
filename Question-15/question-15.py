print("A program that computes the value of 'a+aa+aaa+aaaa' with a given digit as the value of 'a'.")
a = input("Enter the value of 'a': ")

sum = 0
for i in range(1, 5):
    sum += int(a * i)
print(sum)

bin_nums = input("Enter a sequence of comma separated 4 digit binary numbers: ").split(",")
# using loop
ans = []
for num in bin_nums:
    if int(num, 2) % 5 == 0:
        ans.append(num)

# using list comprehension
# ans = [num for num in bin_nums if int(num, 2) % 5 == 0]

print(", ".join(ans))

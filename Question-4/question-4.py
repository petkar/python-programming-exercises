try:
    nums = input("Enter a sequence of comma-separated numbers: ").split(sep=",")
except ValueError:
    print("Enter a valid sequence of comma-separated numbers.")
tup = tuple(nums)

print(nums)
print(tup)

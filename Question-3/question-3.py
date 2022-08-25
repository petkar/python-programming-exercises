try:
    num = int(input("Enter a number: "))
    if num < 1:
        raise ValueError("Enter an integral number greater than 0.")
except ValueError as err:
    print(err)
ans = {}
for i in range(1, num + 1):
    ans[i] = i * i
print(ans)

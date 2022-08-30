ans = []
for i in range(1000, 3001, 2):
    is_invalid = False
    num = []
    for char in str(i):
        if char in "02468":
            num.append(char)
        else:
            is_invalid = True
            break
    if is_invalid:
        continue
    ans.append("".join(num))
print(", ".join(ans))

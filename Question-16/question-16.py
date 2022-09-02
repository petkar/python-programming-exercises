nums = input("Enter a sequence of comma-separated numbers: ").split(",")
ans = [str(int(i)**2) for i in nums if int(i) % 2 == 1]
print(", ".join(ans))

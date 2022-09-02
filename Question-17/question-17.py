print("Program to compute the net amount of a bank account based off transaction log from console input.")
print("D means deposit while W means withdrawal.")
print("eg. D 100\n    W 200\n")
print("Enter net transactions:")
balance = 0
while True:
    prompt = input().split()
    if not prompt:
        break
    transaction = prompt[0].lower()
    amount = int(prompt[1])
    if transaction == "d":
        balance += amount
    elif transaction == "w":
        if balance >= amount:
            balance -= amount
        else:
            print("Insufficient Balance.")
    else:
        print("Invalid input.")
print(balance)

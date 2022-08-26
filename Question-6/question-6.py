from math import sqrt

C, H = 50, 30


def func(d):
    try:
        d = int(d)
    except ValueError:
        print("Enter a valid sequence of comma separated input.")
        print("Example: 100,150,180")
    return str(int(sqrt(2 * C * d / H)))


def main():
    print("This program returns a sequence of outputs for Q in:")
    print("Q = Square root of [(2 * C * D)/H]")
    print("The fixed values of C and H: C = 50 and H = 30.")

    D = input("Enter a sequence of input for D: ").split(",")

    ans = ", ".join(list(map(func, D)))
    print(ans)


if __name__ == "__main__":
    main()

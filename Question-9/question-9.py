def get_lines():
    while True:
        line = input()
        if not line:
            return
        yield line


def print_lines(s):
    print(*(line.upper() for line in s), sep="\n")


print("Enter a sequence of lines as input:")
print_lines(get_lines())

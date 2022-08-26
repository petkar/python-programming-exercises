class MyClass:
    def get_string(self):
        self.s = input("Enter a string: ")

    def print_string(self):
        print(self.s.upper())


def main():
    io = MyClass()
    io.get_string()
    io.print_string()


if __name__ == "__main__":
    main()

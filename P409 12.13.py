class A:
    def __init__(self, i):
        self.i = i

    def __str__(self):
        return "A"

    def __eq__(self, other):
        return self.i == other.i


def main():
    x = A(1)
    y = A(1)
    print(x == y)

main()
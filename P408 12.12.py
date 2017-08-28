class A:
    def __init__(self, i):
        self.i = i

    def __str__(self):
        return "A"


class B(A):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j


def main():
    b = B(1, 2)
    a = A(1)
    print(a)
    print(b)

main()
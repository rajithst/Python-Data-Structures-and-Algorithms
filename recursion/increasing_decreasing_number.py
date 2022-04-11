def decreasing(n):
    if n == 0:
        return
    print(n, end="")
    decreasing(n - 1)


decreasing(5)


def increasing(n):
    if n == 0:
        return
    increasing(n - 1)
    print(n, end="")


increasing(5)

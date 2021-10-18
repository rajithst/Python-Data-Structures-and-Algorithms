def tail(n):
    print("calling tail recursion = " + str(n))
    if n == 0:
        return
    print(n)
    tail(n - 1)


def head(n):
    print("calling head recursion = " + str(n))
    if n == 0:
        return
    head(n - 1)
    print(n)
head(5)
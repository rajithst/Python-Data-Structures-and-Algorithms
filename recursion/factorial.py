def factorial_head_recursion(n):
    if n == 1:
        return 1
    result1 = factorial_head_recursion(n - 1)
    result2 = n * result1
    return result2


print(factorial_head_recursion(4))


def factorial_tail_recursion(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail_recursion(n - 1, n * accumulator)


print(factorial_tail_recursion(4))

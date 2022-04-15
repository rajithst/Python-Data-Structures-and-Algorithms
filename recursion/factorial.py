def factorial_head_recursion(n):
    if n == 1:
        return 1
    # 5! = 5 * 4 * 3 * 2 * 1
    # 5! = 5 * factorial(4)
    # 5! = 5 * 4!
    # 5! = 5 * 4 * 3!
    result = n * factorial_head_recursion(n - 1)
    return result


print(factorial_head_recursion(4))


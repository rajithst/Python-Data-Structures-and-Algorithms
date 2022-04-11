# time complexity: O(2^n)
# space complexity: O(n)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    f1 = fibonacci(n - 1)
    f2 = fibonacci(n - 2)
    return f1 + f2

print(fibonacci(5))
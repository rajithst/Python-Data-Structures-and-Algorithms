def power_function(x, n):
    if n == 0:
        return 1
    # 2^5 = 2 x 2^4
    return x * power_function(x, n - 1)


print(power_function(2, 10))

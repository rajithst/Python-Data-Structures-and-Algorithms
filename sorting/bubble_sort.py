arr = [-1, 10, 15, 3, 52, 19, 5, 19]
n = len(arr)

# do the comparison n-1 times
for times in range(n - 1):
    # after each time finish the iteration,last value is in correct place,so n-times-1 time iterate
    for i in range(n - times - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(arr)

arr = [-1, 10, 15, 3, 5, 19, 5, 19]
n = len(arr)

for i in range(1, n):
    current = arr[i]
    prev = i - 1
    while prev >= 0 and arr[prev] > current:
        arr[prev + 1] = arr[prev]
        prev = prev - 1
    arr[prev + 1] = current

print(arr)

arr = [-1, 10, 15, 3, 5, 19, 5, 19]
n = len(arr)

for position in range(n - 1):
    current = arr[position]
    min_position = position
    for j in range(position, n):
        if arr[j] < arr[min_position]:
            min_position = j
    arr[position], arr[min_position] = arr[min_position], arr[position]
print(arr)

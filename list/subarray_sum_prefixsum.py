arr_list = [-2, 3, 4, -1, 5, -12, 6, 1, 3]


def largest_sub_array(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for k in range(1, len(arr)):
        prefix[k] = prefix[k - 1] + arr[k]

    max_sub_array = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sub_arr_sum = prefix[j] - prefix[i - 1] if i > 0 else prefix[j];
            max_sub_array = max(max_sub_array, sub_arr_sum)
    return max_sub_array


print(largest_sub_array(arr_list))

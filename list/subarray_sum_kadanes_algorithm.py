arr_list = [-2, 3, 4, -1, 5, -12, 6, 1, 3]

max_so_far = max_end_at = arr_list[0]
for i in arr_list[1:]:
    max_end_at = max(max_end_at + i, i)
    max_so_far = max(max_so_far, max_end_at)
print(max_so_far)

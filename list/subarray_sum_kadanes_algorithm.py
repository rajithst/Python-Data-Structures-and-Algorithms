arr_list = [-2, 3, 4, -1, 5, -12, 6, 1, 3]

continues_sum = 0
largest_sum = 0
for i in range(len(arr_list)):
    continues_sum = continues_sum+arr_list[i]
    continues_sum = max(continues_sum,0)
    largest_sum = max(largest_sum,continues_sum)
print(largest_sum)
list1 = [4,5,6]
list2 = [-2,-1,0,7]

index_1 = 0
index_2 = 0

while index_1 < len(list1) and index_2 < len(list2):
    if list1[index_1] > list2[index_2]:
        list1.insert(index_1, list2[index_2])
        index_2 += 1
        index_1 += 1
    else:
        index_1 += 1
if index_2 < len(list2):
    list1 = list1 + list2[index_2:]

print(list1)

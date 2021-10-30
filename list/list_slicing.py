mylist = list(range(10))
print(mylist)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# select elements in index range list[start:end]
print(mylist[0:4])  # 0, 1, 2, 3
print(mylist[3:])  # 3, 4, 5, 6, 7, 8, 9
print(mylist[:3])  # 0 1 2
print(mylist[:])  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# stepped index list[start:stop:step]
mylist = list(range(10))  # define a range of values 0
print(mylist[0:9:2])  # 0, 2, 4, 6, 8
print(mylist[9:0:-2])  # 9, 7, 5, 3, 1

# initialize list elements list[start:end] = [new elements list]
x = list(range(5))
print(x)  # 0, 1, 2, 3, 4
x[1:4] = [45, 21, 83]
print(x)  # 0, 45, 21, 83, 4

# deleting elements from the list
mylist = list(range(10))
print(mylist)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
del mylist[::2]
print(mylist)  # 1, 3, 5, 7, 9

# negative indexing
mylist = list(range(10))
print(mylist)
print(mylist[4:-1])  # 4, 5, 6, 7, 8
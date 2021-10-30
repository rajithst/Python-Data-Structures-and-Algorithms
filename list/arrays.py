import array

myarray = array.array("i", [10, 20, 30, 40, 50, 100, 200])
print(myarray)

# array slicing
print(myarray[1:5])  # 2nd to 5th
print(myarray[:-5])  # beginning to 3rd
print(myarray[5:])  # 6th to end
print(myarray[:])  # beginning to end

# changing first element
myarray[0] = 0
print(myarray)  # array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
myarray[2:5] = array.array('i', [4, 6, 8])
print(myarray)

# append value
myarray.append(4)
print(myarray)

# extend() appends iterable to the end of the array
myarray.extend([5, 6, 7])
print(myarray)

# concatinate arrays
even = array.array('i', [2, 4, 6])
integers = array.array('i')  # creating empty array of integer
integers = myarray + even
print(integers)

# delete element
del integers[2]  # deleting entire array
print(integers)

# remove by value
integers.remove(200)
print(integers)

# pop by index
print(integers.pop(2))
print(integers)

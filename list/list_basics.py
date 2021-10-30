def foo():
    print('Hello from foo()!')

another_list = [5, 'Python', foo, ['yet another list']]

#append
another_list.append("rajith")
print(another_list)

#insert
another_list.insert(0,"newfirst")
print(another_list)

#remove by index
another_list.remove(0)
print(another_list)

#pop - remove element at given index or default last element
another_list.pop(2)
print(another_list)
another_list.pop()
print(another_list)

#reverse
another_list.reverse()
print(another_list)
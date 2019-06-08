# All slice operations return a new list containing requested elements (shallow copy)

squares =  [1,4,9,16,25]

# return all elements
# [start:stop] -> stop not included
squares[:]

# concat squares
squares + [1,2,3]
# -> output = [1,4,9,16,25,1,2,3]

# replace values
squares[1:3] = ['replaced', 'replaced']
print(squares)

# del keyword - remove item from list given its index. 
a = [1,2,3,4,5]

# delete first element
del a[0]
# -> a = [2,3,4,5]

# delete in range
# del a[1:2]
print(a)

# delete all from an index
# del a[2:]
print(a)

# delete all
del a[:]

# List comprehension

# create list nums in range of 0-100
list_of_nums = [number for number in range(100)]

# create tuple nums in range of 0-100
tuple_of_nums = (number for number in range(100))

# create a list with values 1-10 squared
squares = [x ** 2 for x in range(10)]

# join combine elements of two lists into a tuple if they are not equal
print([(i,j) for i in [1,2,3] for j in [4,5,6] if i !=j])

# combine elements of two lists into a tuple if they are not equal (no list comp) 

output = []
for i in [1,2,3]:
    for j in [4,5,6]:
        if i != j:
            output.append((i,j))
print(output)



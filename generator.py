# temporary list that gets created on execution - a blueprint instruction
# still an iterator, but you can only iterate once in a generator
generator = range(100)

print(generator)


def numsFn():
    output = []
    for i in range(100):
        output.append(i)
    print(output)

def numsGen():
    for i in range(100):
        # yield returns values in generators
        yield i



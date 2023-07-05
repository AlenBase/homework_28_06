def enumerate(argument, start=0):
    res = []
    for i in range(len(argument)):
        res.append((i + start, argument[i]))
    yield res

x = enumerate([1,2,3,4],5)
print(list(x))
def zip(*iterable,strict=False):
    res = 0
    minlen = min(len(item) for item in iterable)
    for i in range(minlen):
        items = tuple(item[i] for item in iterable)
        res.append(items)
    yield res

x = zip([1,2,3],[4,5,6])
print(list(x))

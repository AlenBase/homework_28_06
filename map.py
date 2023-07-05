def map(function,iterable):
    res = []
    for i in len(iterable):
        res.append(function(i))
    yield res
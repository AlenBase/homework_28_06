def filter(function,iterable):
    res = []
    if function == None:
        for i in iterable:
            if bool(i) == True:
                res.append(i)
        yield res
    else:
        for i in iterable:
            if function(i):
                res.append(i)
        yield res
        
x = filter(None, [1,2,3,4,5])
print(list(x))

x = filter(lambda i: i % 2 ==0,[1,2,3,4,5])
print(list(x))

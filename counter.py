def counter():
    count = 0

    def in_counter():
        nonlocal count
        count+=1
        yield count
    
    yield in_counter


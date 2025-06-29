def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    current = begin
    for _ in range(end):
        yield current
        current = func(current)
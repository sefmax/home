def prime_generator(end):
    if end > 1:
        for num in range(2, end+1):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                yield num






def add_one(x):
    num = int(''.join(str(digit) for digit in x )) + 1
    new_lst = [int(digit) for digit in str(num)]
    return  new_lst
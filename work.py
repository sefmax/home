def add_one(lst):
    num = int(''.join(str(digit) for digit in lst )) + 1
    new_lst = [int(digit) for digit in str(num)]
    return  new_lst
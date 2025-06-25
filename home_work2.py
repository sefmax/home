def difference_numb(*numbers):
    if numbers == ():
        result = 0

    else:
        result = max(*numbers) - min(*numbers)
    return round(result, 2)

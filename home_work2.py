def difference_numb(*numbers):
    if not numbers:
        result = 0

    else:
        result = max(*numbers) - min(*numbers)
    return round(result, 2)

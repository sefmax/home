def generate_cube_numbers(end):
    for num in range(2, end):
        if num**3 <= end:
            yield num**3
        else:
            return


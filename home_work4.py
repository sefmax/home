def second_index(text, some_str):

    first = text.find(some_str)
    if first == -1:
        return None

    second = text.find(some_str, first + 1)
    if second == -1:
        return None
    return second


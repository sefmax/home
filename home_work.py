import string

inp = input("enter range, example(a-z): ")
start, end = inp.split('-')

letters = string.ascii_letters

start_index = letters.index(start)
end_index = letters.index(end)

if start_index <= end_index:
    result = letters[start_index:end_index + 1]
else:
    result = letters[end_index:start_index + 1]

print(result)


num = int(input("Enter number: "))

while num > 9:
    digits = [int(d) for d in str(num)]
    product = 1
    for d in digits:
        product *= d
    num = product

print(num)
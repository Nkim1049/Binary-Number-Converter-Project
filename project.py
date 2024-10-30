def binaryToDecimal(num):
    if num > 1:
        binaryToDecimal(num // 2)
    print(num % 2, end='')


# decimal number
number = int(input("Enter any decimal number: "))

binaryToDecimal(number)
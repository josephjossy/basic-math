# first impelmentation as a file

def add(num1, num2):
    return int(num1+num2)


def subtract(num1, num2):
    return int(num1-num2)


def multiply(num1, num2):
    return int(num1*num2)


def divide(num1, num2):
    return float(int(num1)/int(num2))


sum = add(2,3)
difference = subtract(2,3)
product = multiply(2,3)
division = divide(2,3)

print(sum,difference,product,division)

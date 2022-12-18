__doc__ = "Implementation of mathematical functions"


from helper import get_float_input
from math import sin, cos, tan, asin, acos, atan, radians, degrees, atan2


class Arithmetic:

    def add(self):
        sum_ = 0
        while True:
            num = get_float_input()
            if num == 0:
                break
            else:
                sum_ += float(num)
        return sum_


    def sub(self):
        num1 = get_float_input()
        num2 = get_float_input()
        return num1 - num2

"""
def mul():
    print("\nEnter 1 to see product")
    mul_ = 1
    while True:
        num = val_input()
        if num == 1.0:
            break
        mul_ *= num
    return decor(round(mul_, 2))


def div():
    try:
        num = input("Enter the numerator: ")
        num1 = float(num)
    except:
        print("Invalid input, try again!")
        num = input("Enter the numerator: ")
        num1 = float(num)

    try:
        num = input("Enter the denominator: ")
        num2 = float(num)
    except:
        print("Invalid input, try again!")
        num = input("Enter the denominator: ")
        num2 = float(num)

    return decor(dec4(num1 / num2))


def even():
    num = val_input()
    if num % 2 == 0:
        return decor("even", "The number is ")
    else:
        return decor("not even", "The number is ")


def quad():
    print("Enter in the form: ax²+bx+c")
    try:
        a1 = input("a? :")
        a = float(a1)
    except:
        print("Invalid input, try again!")
        a1 = input("a? :")
        a = float(a1)

    try:
        b1 = input("b? :")
        b = float(b1)
    except:
        print("Invalid input, try again!")
        b1 = input("b? :")
        b = float(b1)

    try:
        c1 = input("c? :")
        c = float(c1)
    except:
        print("Invalid input, try again!")
        c1 = input("c? :")
        c = float(c1)

    det_ = (b**2) - (4*a*c)

    if det_ < 0:
        return decor("no real root")
    elif det_ == 0:
        root = (-b + (det_**0.5)) / (2*a)
        return decor(dec4(root), "The root of the equation is ")
    else:
        root1 = (-b + (det_**0.5)) / (2*a)
        root2 = (-b - (det_**0.5)) / (2*a)
        return decor(f'{dec4(root1)} and {dec4(root2)}', "The roots of the equation are ")


class Add2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Add2D(self.x + other.x, self.y + other.y)


class Sub2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Sub2D(self.x - other.x, self.y - other.y)


def check_if_prime():
    try:
        num_ = input("Enter a number: ")
        num = int(num_)
    except:
        print("Invalid input, try again!")
        num_ = input("Enter a number: ")
        num = int(num_)

    if num <= 1:
        return decor("not prime", "The number is ")
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return decor("not prime", "The number is ")
    return decor("prime", "The number is ")


def factorial():
    print("\nEnter a number to see its factorial")
    num_ = 1
    while True:
        try:
            val = input("Enter a number:  ")
            num = int(val)
        except:
            print("Invalid input, try again!")
            val = input("Enter a number:  ")
            num = int(val)

        if num < 0:
            print("There is no factorial for negative numbers")
            continue
        else:
            break

    for x in range(1, num+1):
        if num == 1 | num == 0:
            break
        else:
            num_ *= x

    return decor(num_, "The factorial is ")
"""
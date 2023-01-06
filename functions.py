__doc__ = "Implementation of mathematical functions"


from helper import get_float_input
from helper import get_int_input
from math import sin, cos, tan, asin, acos, radians, degrees, atan2


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

    def mul(self):
        mul_ = 1
        while True:
            num = get_float_input()
            if num == 1.0:
                break
            mul_ *= num
        return round(mul_, 2)

    def div(self):
        num1 = get_float_input(msg="Enter the numerator: ")
        num2 = get_float_input(msg="Enter the divisor: ")
        return round(num1 / num2, 4)


class Polynomial:

    def get_quad_roots(self):
        print("Enter in the form: ax²+bx+c")

        a = get_float_input(msg="a? : ")
        b = get_float_input(msg="b? : ")
        c = get_float_input(msg="c? : ")

        det_ = (b**2) - (4*a*c)

        if det_ < 0:
            return "No real root"
        elif det_ == 0:
            root = (-b + (det_**0.5)) / (2*a)
            return f"The root of the equation is {root}"
        else:
            root1 = (-b + (det_**0.5)) / (2*a)
            root2 = (-b - (det_**0.5)) / (2*a)
            return f"The roots of the equation are {root1} and {root2}"


class NumberProperties:

    def is_even(self):
        num = get_int_input()
        return num % 2 == 0

    def is_prime(self):
        num = get_int_input()

        if num <= 1:
            return False

        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False

        return True

    def factorial(self):
        print("Enter a number to see its factorial")
        value = 1
        num = get_int_input()

        if num < 0:
            return "There is no factorial for negative numbers"

        for x in range(1, num+1):
            if num == 1 | num == 0:
                break
            else:
                value *= x

        return f"The factorial is {value}"


class Trignometry:

    def __init__(self, mode="radians") -> None:
        self.mode = mode
    
    def find_sin(self):
        num = get_float_input()
        if self.mode == "degrees":
            return round(sin(radians(num)), 4)
        return round(sin(num), 4)
    
    def find_cos(self):
        num = get_float_input()
        if self.mode == "degrees":
            return round(cos(radians(num)), 4)
        return round(cos(num), 4)
    
    def find_tan(self):
        num = get_float_input()
        if self.mode == "degrees":
            return round(tan(radians(num)), 4)
        return round(tan(num), 4)
    
    def find_sin_inverse(self):
        num = get_float_input()
        if self.mode == "degrees":
            return round(degrees(asin(num)), 4)
        return round(asin(num), 4)
    
    def find_cos_inverse(self):
        num = get_float_input()
        if self.mode == "degrees":
            return round(degrees(acos(num)), 4)
        return round(acos(num), 4)
    
    def find_tan_inverse(self):
        num = get_float_input()
        if self.mode == "degrees":
            return round(degrees(atan2(num)), 4)
        return round(atan2(num), 4)

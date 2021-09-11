"""A customized calculator with cool functions"""

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

import decimal
from math import sin, cos, tan, asin, acos, atan, radians, degrees
import os

# This creates an enclosure for the heading


def decor(func):
    def wrap():
        print("{0:^40}".format("="*20))
        func()
        print("{0:^40}".format("="*20))
    return wrap


@decor
def print_text():
    print("{0:^40}".format("Welcome to MyCalc"))


print_text()

# This creates an enclosure for the answers


def recor(fun):
    def rap():
        print("{0:<40}".format("-"*30))
        fun()
        print("{0:<40}".format("-"*30))
    return rap

# This rounds off the results of multiplication and division to 2 decimal places


def dec1(x):
    return decimal.Decimal(x).quantize(decimal.Decimal("0.00"))

# This rounds off the results of the trigonometry to 4 decimal places


def dec2(x):
    return decimal.Decimal(x).quantize(decimal.Decimal("0.0000"))

# The function for addition


def add():
    print("\ninput '=' when done")
    s = 0
    while True:
        try:
            a = input("Enter numbers to add: ")
            if a == '=':
                break
            s += float(a)
        except:
            print("Invalid input, try again!")
            a = input("Enter numbers to add: ")
            if a == '=':
                break
            s += float(a)
    e = str(s)
    d = "The result is " + e

    @recor
    def print_ext():
        print("{0:^30}".format(d))
    print_ext()

# The function for subtraction


def sub(x, y):
    b = x - y
    c = str(b)
    d = "The result is " + c

    @recor
    def print_ext():
        print("{0:^30}".format(d))
    print_ext()

# The function for multiplication


def mul():
    print("\nEnter 1 to see product")
    b = 1
    while True:
        try:
            e = input("Enter a number: ")
            f = float(e)
            if f == 1.0:
                break
            b *= f
        except:
            print("Invalid input, try again!")
            e = input("Enter a number: ")
            f = float(e)
            if f == 1.0:
                break
            b *= f
    c = str(b)
    a = str(dec1(c))
    d = "The result is " + a

    @recor
    def print_ext():
        print("{0:^30}".format(d))
    print_ext()

# The function for division


def div(x, y):
    b = x / y
    c = str(b)
    a = str(dec1(c))
    d = "The result is " + a

    @recor
    def print_ext():
        print("{0:^30}".format(d))
    print_ext()

# The function for checking even numbers


def even(x):
    if x % 2 == 0.0:
        @recor
        def print_ext():
            print("{0:^30}".format("The number is even"))
        print_ext()
    else:
        @recor
        def print_ext():
            print("{0:^30}".format("The number is not even"))
        print_ext()

# Thw function for solving quadratic equation in the form, ax²+bx+c


def quad(a, b, c):
    for i in range(1):
        s = (b**2) - (4*a*c)
        if s < 0:
            @recor
            def print_ext():
                print("{0:^30}".format("No Real root"))
            print_ext()
            break
        v1 = (-b) + (s**0.5)
        v2 = (-b) - (s**0.5)
        x1 = v1 / (2*a)
        x2 = v2 / (2*a)
        if x1 == x2:
            a = str(x1)
            b = "x is " + a

            @recor
            def print_ext():
                print("{0:^30}".format(b))
            print_ext()
        else:
            a = str(x1)
            b = str(x2)
            c = "x is " + a + " or " + b

            @recor
            def print_ext():
                print("{0:^30}".format(c))
            print_ext()

# Function for adding vectors


class Add2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Add2D(self.x + other.x, self.y + other.y)

# Function for subtracting vectors


class Sub2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Sub2D(self.x - other.x, self.y - other.y)


# Main code
while True:
    print("{0:<30}{1:<30}".format("1.Add", "2.Subtract"))
    print("{0:<30}{1:<30}".format("3.Multiply", "4.Divide"))
    print("{0:<30}{1:<30}".format("5.Check if even", "6.Quadratic"))
    print("{0:<30}{1:<30}".format("7.Vectors",	"8.Check in prime"))
    print("{0:<30}{1:<30}".format("9.Trigonometry", "10.Factorial"))
    print("Enter 'cls' to clear the screen")
    print("Enter 'quit' to exit \n")
    s = input("Enter an option number: ")
    if s == "1":
        add()
    elif s == "2":
        try:
            a = input("Enter a number: ")
            x = float(a)
        except:
            print("Invalid input, try again!")
            a = input("Enter a number: ")
            x = float(a)
        try:
            b = input("Enter another number: ")
            y = float(b)
        except:
            print("Invalid input, try again!")
            b = input("Enter another number: ")
            y = float(b)
        sub(x, y)
    elif s == "3":
        mul()
    elif s == "4":
        try:
            a = input("Enter the numerator: ")
            x = float(a)
        except:
            print("Invalid input, try again!")
            a = input("Enter the numerator: ")
            x = float(a)

        try:
            b = input("Enter the denominator: ")
            y = float(b)
        except:
            print("Invalid input, try again!")
            b = input("Enter the denominator: ")
            y = float(b)

        div(x, y)
    elif s == "5":
        try:
            a = input("Enter a number: ")
            x = int(a)
        except:
            print("Invalid input, try again!")
            a = input("Enter a number: ")
            x = int(a)

        even(x)
    elif s == "6":
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

        quad(a, b, c)
    elif s == "7":
        @recor
        def print_ext():
            print("{0:^30}".format("Welcome to 2D-Vectors Calculator"))
        print_ext()
        print("{0:<30}{1:<30}".format("1.Add", "2.Subtract"))
        print("{0:<30}{1:<30}".format(
            "3.Multiply by scale factor", "4.Dot product"))
        print("To goto main menu, enter: 'home'\n")
        num = str(input("Choose an option: "))

        if num == "1":
            print("Enter vectors as (x,y)")
            print("First vector")
            try:
                a3, a4 = input("x: "), input("y: ")
                a1, a2 = float(a3), float(a4)
            except:
                print("Invalid input, try again!")
                a3, a4 = input("x: "), input("y: ")
                a1, a2 = float(a3), float(a4)

            print("Second vector")
            try:
                b3, b4 = input("x: "), input("y: ")
                b1, b2 = float(b3), float(b4)
            except:
                print("Invalid input, try again!")
                b3, b4 = input("x: "), input("y: ")
                b1, b2 = float(b3), float(b4)

            first = Add2D(a1, a2)
            second = Add2D(b1, b2)
            result = first + second
            a = (result.x, result.y)
            b = str(a)
            c = "The resultant is " + b

            @recor
            def print_ext():
                print("{0:^30}".format(c))
            print_ext()

        elif num == "2":
            print("Enter vectors as (x,y)")
            print("First vector")
            try:
                a3, a4 = input("x: "), input("y: ")
                a1, a2 = float(a3), float(a4)
            except:
                print("Invalid input, try again!")
                a3, a4 = input("x: "), input("y: ")
                a1, a2 = float(a3), float(a4)

            print("Second vector")
            try:
                b3, b4 = input("x: "), input("y: ")
                b1, b2 = float(b3), float(b4)
            except:
                print("Invalid input, try again!")
                b3, b4 = input("x: "), input("y: ")
                b1, b2 = float(b3), float(b4)

            first = Sub2D(a1, a2)
            second = Sub2D(b1, b2)
            result = first + second
            b = (result.x, result.y)
            d = str(b)
            c = "The resultant is " + d

            @recor
            def print_ext():
                print("{0:^30}".format(c))
            print_ext()

        elif num == "3":
            try:
                a1 = input("Enter the factor: ")
                a = float(a1)
            except:
                print("Invalid input, try again!")
                a1 = input("Enter the factor: ")
                a = float(a1)

            print("Enter vectors as (x,y)")
            try:
                b1, c1 = input("x: "), input("y: ")
                b, c = float(b1), float(c1)
            except:
                print("Invalid input, try again!")
                b1, c1 = input("x: "), input("y: ")
                b, c = float(b1), float(c1)

            d = (a*b, a*c)
            e = str(d)
            f = "The resultant is " + e

            @recor
            def print_ext():
                print("{0:^30}".format(f))
            print_ext()

        elif num == "4":
            print("Enter vectors as (x,y)")
            print("First vector")
            try:
                a3, a4 = input("x: "), input("y: ")
                a1, a2 = float(a3), float(a4)
            except:
                print("Invalid input, try again!")
                a3, a4 = input("x: "), input("y: ")
                a1, a2 = float(a3), float(a4)

            print("Second vector")
            try:
                b3, b4 = input("x: "), input("y: ")
                b1, b2 = float(b3), float(b4)
            except:
                print("Invalid input, try again!")
                b3, b4 = input("x: "), input("y: ")
                b1, b2 = float(b3), float(b4)

            c1 = a1*b1
            c2 = a2*b2
            d = c1+c2
            b = str(d)
            c = "The resultant is " + b

            @recor
            def print_ext():
                print("{0:^30}".format(c))
            print_ext()
        elif num == "home":
            print("\n")

    elif s == "8":
        try:
            a1 = input("Enter a number: ")
            a = int(a1)
        except:
            print("Invalid input, try again!")
            a1 = input("Enter a number: ")
            a = int(a1)

        c = 0
        for x in range(1, a):
            if a % x == 0:
                c += 1
        if c == 1:
            @recor
            def print_ext():
                print("{0:^30}".format("The number is prime"))
            print_ext()
        else:
            @recor
            def print_ext():
                print("{0:^30}".format("The number is not prime"))
            print_ext()

    elif s == "9":
        print("{0:<30}{1:<30}".format("1.Degrees", "2.Radians"))
        a = input("Choose your numerical mode: ")
        if a == "1":
            print("{0:<30}{1:<30}".format("1.Sin", "4.Sin inverse"))
            print("{0:<30}{1:<30}".format("2.Cos", "5.Cos inverse"))
            print("{0:<30}{1:<30}".format("3.Tan", "6.Tan inverse"))
            print("To goto main menu, enter: 'home'\n")
            b = input("Select an option: ")
            if b == "1":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = sin(radians(c))
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "2":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = cos(radians(c))
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "3":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = tan(radians(c))
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "4":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = degrees(asin(c))
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "5":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = degrees(acos(c))
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "6":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = degrees(atan(c))
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "home":
                print("\n")
        elif a == "2":
            print("{0:<30}{1:<30}".format("1.Sin", "4.Sin inverse"))
            print("{0:<30}{1:<30}".format("2.Cos", "5.Cos inverse"))
            print("{0:<30}{1:<30}".format("3.Tan", "6.Tan inverse"))
            print("To goto main menu, enter: 'home'\n")
            b = input("Select an option: ")
            if b == "1":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = sin(c)
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "2":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = cos(c)
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "3":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = tan(c)
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "4":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = asin(c)
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "5":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = acos(c)
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "6":
                try:
                    c1 = input("Enter a number: ")
                    c = float(c1)
                except:
                    print("Invalid input, try again!")
                    c1 = input("Enter a number: ")
                    c = float(c1)

                d = atan(c)
                e = str(dec2(d))
                f = "The answer is " + e

                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "home":
                print("\n")
                continue
        else:
            print("Invalid input, try again\n")
    elif s == "10":
        print("\nEnter a number to see its factorial")
        sw = 1
        while True:
            try:
                a1 = input("Enter a number:  ")
                a = int(a1)
            except:
                print("Invalid input, try again!")
                a1 = input("Enter a number:  ")
                a = int(a1)

            if a < 0:
                print("There is no factorial for negative numbers")
                continue
            else:
                break

        for x in range(1, a+1):
            if a == 1 | a == 0:
                er = "The answer is 1"

                @recor
                def print_ext():
                    print("{0:^30}".format(er))
                print_ext()
            sw = x * sw
        d = str(sw)
        e = "The answer is " + d

        @recor
        def print_ext():
            print("{0:^30}".format(e))
        print_ext()
    elif s == "cls":
        os.system("clear")
    elif s == "quit":
        print("Thank you")
        break

    else:
        print("Invalid Input, try again\n")


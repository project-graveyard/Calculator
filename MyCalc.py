"""A customized calculator with cool functions"""

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

from math import sin, cos, tan, asin, acos, atan, radians, degrees, atan2
import os


def decor(x, y=None):
    if y:
        print("{0:^50}".format("-"*50))
        print("{0:^50}".format(y + str(x)))
        print("{0:^50}".format("-"*50))
    else:
        print("{0:^50}".format("-"*50))
        print("{0:^50}".format('The answer is ' + str(x)))
        print("{0:^50}".format("-"*50))


def val_input():
    try:
        num = input("Enter a number: ")
        num_ = float(num)
    except:
        print("Invalid input, try again!")
        num = input("Enter a number: ")
        num_ = float(num)
    return num_


def dec4(x):
    return round(x, 4)


def add():
    print("\ninput '=' when done")
    sum_ = 0
    while True:
        try:
            num = input("Enter numbers to add: ")
            if num == '=':
                break
            sum_ += float(num)
        except:
            print("Invalid input, try again!")
            num = input("Enter numbers to add: ")
            if num == '=':
                break
            sum_ += float(num)
    return decor(sum_)


def sub():
    num1 = val_input()
    num2 = val_input()
    return decor(num1 - num2)


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
        return decor("even")
    else:
        return decor("not even")


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


def vector_input():
    print("Enter vector as (x,y)")
    try:
        x1 = input("x? :")
        x = float(x1)
    except:
        print("Invalid input, try again!")
        x1 = input("x? :")
        x = float(x1)

    try:
        y1 = input("y? :")
        y = float(y1)
    except:
        print("Invalid input, try again!")
        y1 = input("y? :")
        y = float(y1)

    return x, y


def vector_menu():
    print('\n')
    print("{0:^40}".format("="*40))
    print("{0:^40}".format("Welcome to 2D-Vectors Calculator"))
    print("{0:^40}".format("="*40))

    print("{0:<35}{1:<35}".format("1. Add", "2. Subtract"))
    print("{0:<35}{1:<35}".format(
        "3. Multiply by scale factor", "4. Dot product"))
    print("{0:<35}{1:<35}".format(
        "5. Magnitude (1 vector)", "6. Magnitude (2 Vectors)"))
    print("{0:<35}{1:<35}".format(
        "7. Angle between vector & origin", "8. Angle between vectors"))
    print("To goto main menu, press 'ENTER'\n")
    num = str(input("Choose an option: "))

    if num == "1":
        print("First vector")
        vect1 = vector_input()
        print("Second vector")
        vect2 = vector_input()

        first = Add2D(vect1[0], vect1[1])
        second = Add2D(vect2[0], vect2[1])
        result = first + second
        return decor(f'({result.x}, {result.y})', "The sum of the vectors is ")

    elif num == "2":
        print("First vector")
        vect1 = vector_input()
        print("Second vector")
        vect2 = vector_input()

        first = Sub2D(vect1[0], vect1[1])
        second = Sub2D(vect2[0], vect2[1])
        result = first - second
        return decor(f'({result.x}, {result.y})', "The difference of the vectors is ")

    elif num == "3":
        try:
            num_ = input("Enter the factor: ")
            factor = float(num_)
        except:
            print("Invalid input, try again!")
            num_ = input("Enter the factor: ")
            factor = float(num_)

        vect = vector_input()
        result = factor * vect[0], factor * vect[1]
        return decor(f'({result[0]}, {result[1]})', "The resultant is ")

    elif num == "4":
        vect1 = vector_input()
        vect2 = vector_input()

        first = vect1[0] * vect2[0]
        second = vect1[1] * vect2[1]
        result = first + second
        return decor(result, "The dot product is ")

    elif num == "5":
        vect = vector_input()
        result = ((vect[0]**2) + (vect[1]**2))**0.5
        return decor(dec4(result), "The magnitude is ")

    elif num == "6":
        vect1 = vector_input()
        vect2 = vector_input()

        x_ = (vect1[0] - vect2[0])**2
        y_ = (vect1[1] - vect2[1])**2
        result = (x_ + y_)**0.5
        return decor(dec4(result), "The magnitude is ")

    elif num == "7":
        vect = vector_input()
        result = degrees(atan2(vect[1], vect[0]))
        return decor(dec4(result), "The angle is ")

    elif num == "8":
        vect1 = vector_input()
        vect2 = vector_input()
        mag1 = ((vect1[0]**2) + (vect1[1]**2))**0.5
        mag2 = ((vect2[0]**2) + (vect2[1]**2))**0.5
        dot_p = ((vect1[0] * vect2[0]) + (vect1[1] * vect2[1]))
        result = degrees(acos(dot_p / (mag1 * mag2)))
        return decor(dec4(result), "The angle is ")
    else:
        print("Invalid input, try again\n")


def check_if_prime():
    try:
        num_ = input("Enter a number: ")
        num = int(num_)
    except:
        print("Invalid input, try again!")
        num_ = input("Enter a number: ")
        num = int(num_)

    counter = 0
    for x in range(1, num):
        if num % x == 0:
            counter += 1
    if counter == 1:
        return decor("prime", "The number is ")
    else:
        return decor("not prime", "The number is ")


def trig_input():
    try:
        num_ = input("Enter a number: ")
        num = float(num_)
    except:
        print("Invalid input, try again!")
        num_ = input("Enter a number: ")
        num = float(num_)

    return num


def trig_menu():
    print("{0:<30}{1:<30}".format("1.Degrees", "2.Radians"))
    option_1 = input("Choose your numerical mode: ")
    if option_1 == "1":
        print('\nDegrees')
        print("{0:<30}{1:<30}".format("1.Sin", "4.Sin inverse"))
        print("{0:<30}{1:<30}".format("2.Cos", "5.Cos inverse"))
        print("{0:<30}{1:<30}".format("3.Tan", "6.Tan inverse"))
        print("To goto main menu, enter: 'home'\n")
        option_2 = input("Select an option: ")
        if option_2 == "1":
            val = trig_input()
            result = sin(radians(val))
            return decor(dec4(result))

        elif option_2 == "2":
            val = trig_input()
            result = cos(radians(val))
            return decor(dec4(result))

        elif option_2 == "3":
            val = trig_input()
            result = tan(radians(val))
            return decor(dec4(result))

        elif option_2 == "4":
            val = trig_input()
            result = degrees(asin(val))
            return decor(dec4(result))

        elif option_2 == "5":
            val = trig_input()
            result = degrees(acos(val))
            return decor(dec4(result))

        elif option_2 == "6":
            val = trig_input()
            result = degrees(atan(val))
            return decor(dec4(result))

    elif option_1 == "2":
        print('\nRadians')
        print("{0:<30}{1:<30}".format("1.Sin", "4.Sin inverse"))
        print("{0:<30}{1:<30}".format("2.Cos", "5.Cos inverse"))
        print("{0:<30}{1:<30}".format("3.Tan", "6.Tan inverse"))
        print("To goto main menu, enter: 'home'\n")
        option_2 = input("Select an option: ")
        if option_2 == "1":
            val = trig_input()
            result = sin(val)
            return decor(dec4(result))

        elif option_2 == "2":
            val = trig_input()
            result = cos(val)
            return decor(dec4(result))
        
        elif option_2 == "3":
            val = trig_input()
            result = tan(val)
            return decor(dec4(result))
        
        elif option_2 == "4":
            val = trig_input()
            result = asin(val)
            return decor(dec4(result))

        elif option_2 == "5":
            val = trig_input()
            result = acos(val)
            return decor(dec4(result))
        
        elif option_2 == "6":
            val = trig_input()
            result = atan(val)
            return decor(dec4(result))
    else:
        print("Invalid input, try again\n")


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



print("{0:^40}".format("="*20))
print("{0:^40}".format("Welcome to MyCalc"))
print("{0:^40}".format("="*20))
while True:
    print("{0:<30}{1:<30}".format("1. Add", "2. Subtract"))
    print("{0:<30}{1:<30}".format("3. Multiply", "4. Divide"))
    print("{0:<30}{1:<30}".format("5. Check if even", "6. Quadratic"))
    print("{0:<30}{1:<30}".format("7. Vectors",	"8. Check in prime"))
    print("{0:<30}{1:<30}".format("9. Trigonometry", "10. Factorial"))
    print("Enter 'cls' to clear the screen")
    print("Enter 'quit' to exit \n")
    option = input("Enter an option number: ")
    if option == "1":
        add()

    elif option == "2":
        sub()

    elif option == "3":
        mul()

    elif option == "4":
        div()

    elif option == "5":
        even()

    elif option == "6":
        quad()

    elif option == "7":
        vector_menu()

    elif option == "8":
        check_if_prime()

    elif option == "9":
        trig_menu()

    elif option == "10":
        factorial()

    elif option == "cls":
        os.system("clear")

    elif option == "quit":
        print("Thank you")
        break

    else:
        print("Invalid Input, try again\n")

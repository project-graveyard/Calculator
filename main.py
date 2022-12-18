#!/usr/bin/env python3

__doc__ = "A customized calculator with cool functions"
__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

from functions import Arithmetic
from helper import output
# from functions import Vectors
import os

arithmetic = Arithmetic()


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
        print()
        print("input 0 when done")
        value = arithmetic.add()
        output(f"The sum of the numbers are {value}")   

    elif option == "2":
        print()
        value = arithmetic.sub()
        output(f"The difference is {value}")

    elif option == "3":
        print()
        print("Enter 1 to see product")
        value = arithmetic.mul()

    # elif option == "4":
    #     div()

    # elif option == "5":
    #     even()

    # elif option == "6":
    #     quad()

    # elif option == "7":
    #     vector_menu()

    # elif option == "8":
    #     check_if_prime()

    # elif option == "9":
    #     trig_menu()

    # elif option == "10":
    #     factorial()


    elif option == "cls":
        os.system("clear")

    elif option == "quit":
        print("Thank you")
        break

    else:
        print("Invalid Input, try again\n")

#!/usr/bin/env python3

__doc__ = "A customized calculator with cool functions"
__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

from functions import Arithmetic
from functions import Polynomial
from functions import NumberProperties
from helper import output
from submenus import trig_menu
from submenus import vector_menu
import os
from time import sleep


arithmetic = Arithmetic()
polynomial = Polynomial()
num_property = NumberProperties()


print("="*50)
print("{0:^50}".format("Welcome to MyCalc"))
print("="*50)

while True:
    print("{0:^50}".format("Main Menu"))
    print("-"*50)
    print("{0:<30}{1:<30}".format("1. Add", "2. Subtract"))
    print("{0:<30}{1:<30}".format("3. Multiply", "4. Divide"))
    print("{0:<30}{1:<30}".format("5. Check if even", "6. Check if prime"))
    print("{0:<30}{1:<30}".format("7. Quadratic equation",	"8. Factorial"))
    print("{0:<30}{1:<30}".format("9. Trigonometry", "10. Vectors"))
    print()
    print("[!] Enter 'cls' to clear the screen")
    print("[!} Enter 'quit' to exit \n")

    option = input("Enter an option number: ")

    if option == "1":
        print()
        print("[!] Input 0 when done\n")
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
        output(f"The product is {value}")

    elif option == "4":
        print()
        value = arithmetic.div()
        output(f"The quotient is {value}")

    elif option == "5":
        print()
        is_even = num_property.is_even()
        if is_even:
            output("The number is even")
        else:
            output("The number is odd")

    elif option == "6":
        print()
        is_prime = num_property.is_prime()
        if is_prime:
            output("The number is prime")
        else:
            output("The number is not prime")

    elif option == "7":
        print()
        msg = polynomial.get_quad_roots()
        output(msg)

    elif option == "8":
        print()
        value = num_property.factorial()
        output(value)

    elif option == "9":
        trig_menu()

    elif option == "10":
        vector_menu()

    elif option == "cls":
        os.system("clear")

    elif option == "quit":
        print("\nThank you for using MyCalc")
        break

    else:
        print("Invalid option, try again\n")
        sleep(1)

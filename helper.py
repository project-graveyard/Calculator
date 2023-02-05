__doc__ = "Helper functions for calculator"
from time import sleep


def get_float_input(msg="Enter a number: "):
    try:
        num = input(msg)
        num_ = float(num)
    except ValueError:
        print("Invalid input, try again!")
        sleep(1)
        num = input(msg)
        num_ = float(num)
    return num_


def get_int_input(msg="Enter a number: "):
    try:
        num = input(msg)
        num_ = int(num)
    except ValueError:
        print("Invalid input, try again!")
        sleep(1)
        num = input(msg)
        num_ = int(num)
    return num_


def vector_input():
    print("Enter vector as (x,y)")
    x = get_float_input(msg="x? : ")
    y = get_float_input(msg="y? : ")
    return x, y


def output(data):
    print("{0:^50}".format("-"*50))
    print("{0:^50}".format(data))
    print("{0:^50}".format("-"*50))
    print()
    sleep(1.5)

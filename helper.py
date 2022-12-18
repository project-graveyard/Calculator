__doc__ = "Helper functions for calculator"


def get_float_input():
    try:
        num = input("Enter a number: ")
        num_ = float(num)
    except:
        print("Invalid input, try again!")
        num = input("Enter a number: ")
        num_ = float(num)
    return num_


def output(data):
    print("{0:^50}".format("-"*50))
    print("{0:^50}".format(data))
    print("{0:^50}".format("-"*50))


# def trig_input():
#     try:
#         num_ = input("Enter a number: ")
#         num = float(num_)
#     except:
#         print("Invalid input, try again!")
#         num_ = input("Enter a number: ")
#         num = float(num_)

#     return num

# def vector_input():
#     print("Enter vector as (x,y)")
#     try:
#         x1 = input("x? :")
#         x = float(x1)
#     except:
#         print("Invalid input, try again!")
#         x1 = input("x? :")
#         x = float(x1)

#     try:
#         y1 = input("y? :")
#         y = float(y1)
#     except:
#         print("Invalid input, try again!")
#         y1 = input("y? :")
#         y = float(y1)

#     return x, y

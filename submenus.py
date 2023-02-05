__doc__ = "Calculator sub menu functions"

from helper import output
from helper import vector_input
from helper import get_float_input
from time import sleep
from functions import Trignometry
import vectors
from math import degrees, atan2, acos


deg_trig = Trignometry("degrees")
rad_trig = Trignometry()


def trig_menu():
    print()
    print("{0:30}".format("Choose your numerical mode"))
    print("-"*30)
    print("{0:<15}{1:<15}".format("1. Degrees", "2. Radians"))

    option_1 = input("option: ")

    if option_1 == "1":
        print()
        print("{0:^30}".format("Trignometry Menu"))
        print("-"*30)
        print("{0:<15}{1:<15}".format("1. Sin", "4. Sin inverse"))
        print("{0:<15}{1:<15}".format("2. Cos", "5. Cos inverse"))
        print("{0:<15}{1:<15}".format("3. Tan", "6. Tan inverse"))

        print("\nIn degrees mode...\n")
        option_2 = input("Select an option: ")

        if option_2 == "1":
            print()
            val = deg_trig.find_sin()
            output(f"The answer is {val}")
        elif option_2 == "2":
            print()
            val = deg_trig.find_cos()
            output(f"The answer is {val}")
        elif option_2 == "3":
            print()
            val = deg_trig.find_tan()
            output(f"The answer is {val}")
        elif option_2 == "4":
            print()
            val = deg_trig.find_sin_inverse()
            output(f"The answer is {val} degrees")
        elif option_2 == "5":
            print()
            val = deg_trig.find_cos_inverse()
            output(f"The answer is {val} degrees")
        elif option_2 == "6":
            print()
            val = deg_trig.find_tan_inverse()
            output(f"The answer is {val} degrees")
        else:
            print("\nInvalid input, try again!\n")
            sleep(1)

    elif option_1 == "2":
        print()
        print("{0:^30}".format("Trignometry Menu"))
        print("-"*30)
        print("{0:<15}{1:<15}".format("1. Sin", "4. Sin inverse"))
        print("{0:<15}{1:<15}".format("2. Cos", "5. Cos inverse"))
        print("{0:<15}{1:<15}".format("3. Tan", "6. Tan inverse"))

        print("\nIn radians mode...\n")
        option_2 = input("Select an option: ")

        if option_2 == "1":
            print()
            val = rad_trig.find_sin()
            output(f"The answer is {val}")
        elif option_2 == "2":
            print()
            val = rad_trig.find_cos()
            output(f"The answer is {val}")
        elif option_2 == "3":
            print()
            val = rad_trig.find_tan()
            output(f"The answer is {val}")
        elif option_2 == "4":
            print()
            val = rad_trig.find_sin_inverse()
            output(f"The answer is {val} radians")
        elif option_2 == "5":
            print()
            val = rad_trig.find_cos_inverse()
            output(f"The answer is {val} radians")
        elif option_2 == "6":
            print()
            val = rad_trig.find_tan_inverse()
            output(f"The answer is {val} radians")
        else:
            print("\nInvalid input, try again!\n")
            sleep(1)

    else:
        print("\nInvalid input, try again!\n")
        sleep(1)


def vector_menu():
    print()
    print("{0:^65}".format("2D-Vectors Calculator"))
    print("-"*65)

    print("{0:<35}{1:<30}".format("1. Add", "2. Subtract"))
    print("{0:<35}{1:<30}".format(
        "3. Scalar multiplication", "4. Dot product"))
    print("{0:<35}{1:<30}".format(
        "5. Magnitude (1 vector)", "6. Magnitude (2 Vectors)"))
    print("{0:<35}{1:<30}".format(
        "7. Angle between vector & origin", "8. Angle between 2 vectors"))
    print()

    option = input("Choose an option: ")

    if option == "1":
        print("\nFirst vector")
        vect1 = vector_input()
        print("\nSecond vector")
        vect2 = vector_input()

        first_vector = vectors.Make2D(vect1[0], vect1[1])
        second_vector = vectors.Make2D(vect2[0], vect2[1])
        result_vector = first_vector + second_vector

        output(
            f"The sum of the vectors is ({result_vector.x}, {result_vector.y})"
        )

    elif option == "2":
        print("\nFirst vector")
        vect1 = vector_input()
        print("\nSecond vector")
        vect2 = vector_input()

        first_vector = vectors.Make2D(vect1[0], vect1[1])
        second_vector = vectors.Make2D(vect2[0], vect2[1])
        result_vector = first_vector - second_vector

        output(
            f"The difference vector is ({result_vector.x}, {result_vector.y})"
        )

    elif option == "3":
        vect = vector_input()
        factor = get_float_input("Scale factor: ")
        result_vector = factor * vect[0], factor * vect[1]
        output(f"The resultant is ({result_vector[0]}, {result_vector[1]})")

    elif option == "4":
        print("\nFirst vector")
        vect1 = vector_input()
        print("\nSecond vector")
        vect2 = vector_input()

        result = vectors.dot_product(vect1, vect2)
        output(f"The dot product is {result}")

    elif option == "5":
        vect = vector_input()
        result = vectors.magnitude(vect)
        output(f"The magnitude is {result}")

    elif option == "6":
        print("\nFirst vector")
        vect1 = vector_input()
        print("\nSecond vector")
        vect2 = vector_input()

        x = (vect1[0] - vect2[0]) ** 2
        y = (vect1[1] - vect2[1]) ** 2

        result = (x + y) ** 0.5
        output(f"The magnitude is {result}")

    elif option == "7":
        vect = vector_input()
        angle = degrees(atan2(vect[1], vect[0]))
        output(f"The angle is {angle} degrees")

    elif option == "8":
        print("\nFirst vector")
        vect1 = vector_input()
        print("\nSecond vector")
        vect2 = vector_input()

        mag1 = vectors.magnitude(vect1)
        mag2 = vectors.magnitude(vect2)
        dot_p = vectors.dot_product(vect1, vect2)
        result = degrees(acos(dot_p / (mag1 * mag2)))
        output(f"The angle is {round(result, 4)}")

    else:
        print("\nInvalid input, try again!\n")
        sleep(1)

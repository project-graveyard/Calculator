__doc__ = "Calculator sub menu functions"

from helper import output
from time import sleep
from functions import Trignometry


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
            sleep(1.5)
    
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
            sleep(1.5)

    else:
        print("\nInvalid input, try again!\n")
        sleep(1.5)


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

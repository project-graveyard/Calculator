"""A customized calculator with cool functions"""

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

import decimal
from math import sin,cos,tan,asin,acos,atan,radians,degrees

#This creates an enclosure for the heading
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

#This creates an enclosure for the answers
def recor(fun):
  def rap():
    print("{0:<40}".format("-"*30))
    fun()
    print("{0:<40}".format("-"*30))
  return rap

#This rounds off the results of multiplication and division to 2 decimal places
def dec1(x):
    return decimal.Decimal(x).quantize(decimal.Decimal("0.00"))

#This rounds off the results of the trigonometry to 4 decimal places
def dec2(x):
    return decimal.Decimal(x).quantize(decimal.Decimal("0.0000"))

#The function for addition
def add():
    print("Enter numbers to add")
    s = 0
    while True:
        a = input("input '=' when done: ")
        if a == '=':
            break
        else:
            s += float(a)
    e = str(s)
    d = "The result is " + e
    @recor
    def print_ext():
        print("{0:^30}".format(d))
    print_ext()

#The function for subtraction    
def sub(x,y):
    b = x-y
    c = str(b)
    d = "The result is " + c
    @recor
    def print_ext():
        print("{0:^30}".format(d))
    print_ext()

#The function for multiplication    
def mul(x,y):
    b = x*y
    c = str(b)
    a = str(dec1(c))
    d = "The result is " + a
    @recor
    def print_ext():
        print("{0:^30}".format(d))
    print_ext()

#The function for division    
def div(x,y):
    b = x/y
    c = str(b)
    a = str(dec1(c))
    d = "The result is " + a
    @recor
    def print_ext():
        print("{0:^30}".format(d))
    print_ext()

#The function for checking even numbers    
def even(x):
    if x%2==0:
        @recor
        def print_ext():
            print("{0:^30}".format("The number is even"))
        print_ext()
    else:
        @recor
        def print_ext():
            print("{0:^30}".format("The number is not even"))
        print_ext()

#Thw function for solving quadratic equation in the form, ax²+bx+c
def quad(a,b,c):
    for i in range(1):
      s = (b**2)-(4*a*c)
      if s<0:
        @recor
        def print_ext():
          print("{0:^30}".format("No Real root"))
        print_ext()
        break
      v1 = (-b)+(s**0.5)
      v2 = (-b)-(s**0.5)
      x1 = v1/(2*a)
      x2 = v2/(2*a)
      if x1==x2:
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

#Function for adding vectors          
class Add2D:
   def __init__(self, x, y):
     self.x = x
     self.y = y
   def __add__(self, other):
     return Add2D(self.x + other.x, self.y + other.y)

#Function for subtracting vectors    
class Sub2D:
   def __init__(self, x, y):
     self.x = x
     self.y = y
   def __add__(self, other):
     return Sub2D(self.x - other.x, self.y - other.y)

#Main code
while True:
    print("{0:<30}{1:<30}".format("1.Add","2.Subtract"))
    print("{0:<30}{1:<30}".format("3.Multiply","4.Divide"))
    print("{0:<30}{1:<30}".format("5.Check if even","6.Quadratic"))
    print("{0:<30}{1:<30}".format("7.Vectors","8.Check in prime"))
    print("{0:<30}{1:<30}".format("9.Trigonometry","10.Factorial"))
    print("Enter 'quit' to exit \n")
    s=input("Enter an option number: ")
    if s=="1":
        add()
    elif s=="2":
        a=float(input("Enter a number: "))
        b=float(input("Enter another number: "))
        sub(a,b)
    elif s=="3":
        a=float(input("Enter a number: "))
        b=float(input("Enter another number: "))
        mul(a,b)
    elif s=="4":
        a=float(input("Enter the numerator: "))
        b=float(input("Enter the denominator: "))
        div(a,b)
    elif s=="5":
        a=float(input("Enter a number: "))
        even(a)
    elif s=="6":
        print("Enter in the form: ax²+bx+c")
        a=float(input("a? :"))
        b=float(input("b? :"))
        c=float(input("c? :"))
        quad(a,b,c)
    elif s=="7":
        @recor
        def print_ext():
            print("{0:^30}".format("Welcome to 2D-Vectors Calculator"))
        print_ext()
        print("{0:<30}{1:<30}".format("1.Add","2.Subtract"))
        print("{0:<30}{1:<30}".format("3.Multiply by scale factor","4.Dot product"))
        print("To goto main menu, enter: 'home'\n")
        num=str(input("Choose an option: "))

        if num=="1":
          print("Enter vectors as (x,y)")
          print("First vector")
          a1,a2=float(input("x: ")), float(input("y: "))
          print("Second vector")
          b1,b2=float(input("x: ")), float(input("y: "))
          first = Add2D(a1,a2)
          second = Add2D(b1,b2)
          result = first + second
          a=(result.x,result.y)
          b = str(a)
          c = "The resultant is " + b
          @recor
          def print_ext():
            print("{0:^30}".format(c))
          print_ext()

        elif num=="2":
          print("Enter vectors as (x,y)")
          print("First vector")
          a1,a2=float(input("x: ")), float(input("y: "))
          print("Second vector")
          b1,b2=float(input("x: ")), float(input("y: "))
          first = Sub2D(a1,a2)
          second = Sub2D(b1,b2)
          result = first + second
          b=(result.x,result.y)
          d = str(b)
          c = "The resultant is " + d
          @recor
          def print_ext():
            print("{0:^30}".format(c))
          print_ext()

        elif num=="3":
          a=float(input("Enter the factor: "))
          print("Enter vectors as (x,y)")
          b,c = float(input("x: ")), float(input("y: "))
          d=(a*b,a*c)
          e = str(d)
          f = "The resultant is " + e
          @recor
          def print_ext():
            print("{0:^30}".format(f))
          print_ext()

        elif num=="4":
          print("Enter vectors as (x,y)")
          print("First vector")
          a1,a2=float(input("x: ")), float(input("y: "))
          print("Second vector")
          b1,b2=float(input("x: ")), float(input("y: "))
          c1=a1*b1
          c2=a2*b2
          d=c1+c2
          b = str(d)
          c = "The resultant is " + b
          @recor
          def print_ext():
            print("{0:^30}".format(c))
          print_ext()
        elif num == "home":
            print("\n")

    elif s == "8":
        a = int(input("Enter a number: "))
        c = 0
        for x in range(1,a):
            if a%x == 0:
                c+=1
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
        print("{0:<30}{1:<30}".format("1.Degrees","2.Radians"))
        a = input("Choose your numerical mode: ")
        if a == "1":
            print("{0:<30}{1:<30}".format("1.Sin","4.Sin inverse"))
            print("{0:<30}{1:<30}".format("2.Cos","5.Cos inverse"))
            print("{0:<30}{1:<30}".format("3.Tan","6.Tan inverse"))
            print("To goto main menu, enter: 'home'\n")
            b = input("Select an option: ")
            if b == "1":
                c = float(input("Enter a number: "))
                d = sin(radians(c))
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "2":
                c = float(input("Enter a number: "))
                d = cos(radians(c))
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "3":
                c = float(input("Enter a number: "))
                d = tan(radians(c))
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "4":
                c = float(input("Enter a number: "))
                d = degrees(asin(c))
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "5":
                c = float(input("Enter a number: "))
                d = degrees(acos(c))
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "6":
                c = float(input("Enter a number: "))
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
            print("{0:<30}{1:<30}".format("1.Sin","4.Sin inverse"))
            print("{0:<30}{1:<30}".format("2.Cos","5.Cos inverse"))
            print("{0:<30}{1:<30}".format("3.Tan","6.Tan inverse"))
            print("To goto main menu, enter: 'home'\n")
            b = input("Select an option: ")
            if b == "1":
                c = float(input("Enter a number: "))
                d = sin(c)
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "2":
                c = float(input("Enter a number: "))
                d = cos(c)
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "3":
                c = float(input("Enter a number: "))
                d = tan(c)
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "4":
                c = float(input("Enter a number: "))
                d = asin(c)
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "5":
                c = float(input("Enter a number: "))
                d = acos(c)
                e = str(dec2(d))
                f = "The answer is " + e
                @recor
                def print_ext():
                    print("{0:^30}".format(f))
                print_ext()
            elif b == "6":
                c = float(input("Enter a number: "))
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
    elif s=="10":
        print("Enter a number to see its factorial")
        a = int(input("Enter a number:  "))
        if a < 0:
        	raise ValueError("There is no value for negative numbers")
        sw = 1
        for x in range (1, a+1):
            if a == 1 | a == 0:
                er = "The answer is 1"
                @recor
                def print_ext():
                    print("{0:^30}".format(er))
                print_ext()
            sw =  x * sw
        d = str(sw)
        e = "The answer is " + d
        @recor
        def print_ext():
            print("{0:^30}".format(e))
        print_ext()
    elif s=="quit":
        print("Thank you")
        break
    else:
        print("Invalid Input, try again\n")
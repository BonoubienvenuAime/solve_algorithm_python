# This is a sample Python script.
import fibonacci
import random
import calendar
import math


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def addition():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    sum_result = num1 + num2
    print(f" sum: {num1} + {num2} = {sum_result}")


def division():
    num3 = float(input('Enter the dividend for division: '))
    num4 = float(input('Enter the divisor for division: '))
    if num4 == 0:
        print("Error: Division by zero is not allowed")
    else:
        div_result = num3 / num4
        print(f"Division: {num3} / {num4} = {div_result}")


def area_triangle():
    base = float(input('Enter the base length: '))
    height = float(input('Enter the height of the triangle: '))
    area = (base * height) / 2
    print(f"The area of the triangle is : {area}")


def swap_two_variables():
    var1 = input('Enter the first variable: ')
    var2 = input('Enter the second variable: ')
    print(f"Original values are: var1 = {var1}, var2 = {var2}")
    tmp = var1
    var1 = var2
    var2 = tmp
    print(f"Swapped values are: var1 = {var1}, var2 = {var2}")


def random_number():
    print(f"Random number: {random.randint(1, 100)}")


def kilometer_mile():
    kilometer = float(input('Enter distance the kilometer: '))
    miles = kilometer * 0.621371
    print(f"The distance of the miles is : {miles}")


def convert_celcius_to_fahrenheit():
    celcius = float(input('Enter temperature in celcius: '))
    fahrenheit = (celcius * 9 / 5) + 32
    print(f"Celcius {celcius} to fahrenheit is {fahrenheit}")


def display_calendar():
    year = int(input('Enter the year: '))
    month = int(input('Enter the month: '))
    cal = calendar.month(year, month)
    print(cal)


def solve_quadratic_equation():
    a = float(input('Enter the value of a '))
    b = float(input('Enter the value of b '))
    c = float(input('Enter the value of c '))
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(delta)) / (2 * a)
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        print(f"the solution of this equation is {x} ")
    else:
        racine_delta = math.sqrt(delta)
        x1 = (-b - racine_delta) / (2 * a)
        x2 = (-b + racine_delta) / (2 * a)
        print(f"the solution is x1 = {x1}, x2 = {x2}")


def swap_two_variables_without_temp_variable():
    a = 5
    b = 10
    a, b = b, a
    print("After swapping: ")
    print(" a = ", a)
    print(" b = ", b)


def check_number():
    number = float(input('Enter the number: '))
    if number > 0:
        print(f"the number {number} is positive")
    elif number == 0:
        print(f"the number {number} is zero")
    else:
        print("the number {number} is negative")


def check_number_odd_even():
    number = int(input('Enter the number: '))
    if number % 2 == 0:
        print(f"the number {number} is even ")
    else:
        print(f"the number {number} is odd ")


def check_leap_year():
    year = int(input('Enter a year: '))
    if (year % 100 == 0) and (year % 400 == 0):
        print(f"the year {year} is leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"the year {year} is a leap year ")
    else:
        print(f"the year {year} is not a leap year")


def check_prime_number():
    number = int(input('Enter the number: '))
    is_prime_number = True
    for index in range(1, number):
        if (number % index == 0) and (index != 1):
            print(f"the number {number} is not a prime ")
            is_prime_number = False
            break
    if is_prime_number:
        print(f"{number} is a prime number")


def factoriel():
    number = int(input("Enter the number: "))
    fact = 1
    if number < 0:
        print("Error: negative number")
    elif number == 0:
        print(f"the factorial of {number} is 1")
    else:
        for i in range(1, number + 1):
            fact = fact * i
        print(f"the factoriel of {number} is {fact}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # solve_quadratic_equation()
    # swap_two_variables_without_temp_variable()
    # check_number()
    # check_leap_year()
    # check_prime_number()
    factoriel()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

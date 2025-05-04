#Q1:- Write a program that will convert celsius value to fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")

# Q2:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
def swap_to_numbers(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    return swap_to_numbers

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
print("After swapping:",num2,num1)

# Q3:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

print("Enter the coordinates of the first point (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Enter the coordinates of the second point (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distance = calculate_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between the points is: {distance:.2f}")

#Q4:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
def calculate_simple_interest(principal,rate_of_interest,time_period):
    simple_interest=(principal*rate_of_interest*time_period)/100
    return simple_interest
principal=float(input("Enter value of principal:"))
rate_of_interest=float(input("Enter value of rate_of_interest:"))
time_period=float(input("Enter value of time_period:"))
simple_interest=calculate_simple_interest(principal,rate_of_interest,time_period)
print(f"The simple interest of:",simple_interest)

"""Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
For example:
    Input:
        heads -> 4
        legs -> 12
    Output:
        dogs -> 2
        chicken -> 2"""

def add(a,b=0,c=6):
    return a+b+c
print(add(5,9))

def fact(n):
    total=1
    for i in range(n):
        total=total*i
        return total

    
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

     
def str(n):
    for i in range(1,n):
        print(i*"*")
        

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

#Q.5:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
#For example:
#   Input:
#       heads -> 4
#       legs -> 12
#   Output:
#       dogs -> 2
#       chicken -> 2
total_heads = int(input("Enter the total number of heads: "))
total_legs = int(input("Enter the total number of legs: "))
chickens = (4 * total_heads - total_legs) // 2
dogs = total_heads - chickens
if chickens < 0 or dogs < 0 or 2 * chickens + 4 * dogs != total_legs:
    print("No valid solution exists with the given heads and legs.")
else:
    print(f"Number of chickens: {chickens}")
    print(f"Number of dogs: {dogs}")
    
# Q.6:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
n = int(input("Enter the value of n: "))
sum_of_squares = 0
for i in range(1, n + 1):
    sum_of_squares += i ** 2
print("The sum of squares of first", n, "natural numbers is:", sum_of_squares)

#Q.7:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
# Get inputs from the user
a1 = int(input("Enter the first term: "))
a2 = int(input("Enter the second term: "))
n = int(input("Enter the term number to find: "))
d = a2 - a1
an = a1 + (n - 1) * d
print(f"The {n}th term of the arithmetic series is: {an}")

#Q.8:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
def sum_of_fractions(a,b,c,d):
  sum_of_fractions = ((a*b)+(c*d))/(b*d)
  return sum_of_fractions
a=int(input("Enter the numerator of the first fraction: "))
b=int(input("Enter the denominator of the second fraction: "))
c=int(input("Enter the numerator of the third fraction: "))
d=int(input("Enter the denominator of the forth fraction: "))
sum = sum_of_fractions(a,b,c,d)
print("The sum of the fractions is:",sum)


# Q.9:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
#Input:
#Dimensions of the milk tank<br>
#H = 20cm, L = 20cm, B = 20cm
#Dimensions of the glass<br>
#h = 3cm, r = 1cm
# Get inputs from the user
height = float(input("Enter the height of the milk tank (cm): "))
width = float(input("Enter the width of the milk tank (cm): "))
breadth = float(input("Enter the breadth of the milk tank (cm): "))
glass_volume = 250 
tank_volume = height * width * breadth
number_of_glasses = tank_volume // glass_volume 
print(f"The number of full glasses of milk that can be obtained is: {int(number_of_glasses)}")

####1

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")

###2
def swap_to_numbers(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    return swap_to_numbers

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
print("After swapping:",num2,num1)
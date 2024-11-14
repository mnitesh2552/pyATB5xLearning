# Take 2 input from user and print quotient and remainder
num1 = int(input("Enter the first number (divident):"))
num2 = int(input("Enter the second number (divisor):"))
quotient = num1 // num2  # using  floor division to get the quotient
remainder = num1 % num2  # Using modulo to get the remainder
print(f"quotient (Q) -> {quotient}")
print(f"remainder (R) -> {remainder}")

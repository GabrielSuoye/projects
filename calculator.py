# Python Calculator 

num1 = float(input("Enter the first value: "))
operator = input("Enter an operator (+ - / *): ")
num2 = float(input("Enter the second value: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result = num1 / num2
elif operator == "*":
    result = num1 * num2
else:
    print("Invalid operator")

print(round(result, 3)) 

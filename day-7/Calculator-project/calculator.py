# (Basic Simple Calculator)
print("Simple Calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /, %,//,**,mod,min,max,avg): ")

# Addition Method
if operation == "+":
    print("Result:", num1 + num2)

# Subtraction Method
elif operation == "-":
    print("Result:", num1 - num2)

# Multiplication Method
elif operation == "*":
    print("Result:", num1 * num2)

# Division Method
elif operation == "/":
    print("Result:", num1 / num2)

# Percentage Method
elif operation == "%":
    print("Result:", (num1 / 100) * num2)

# Floor Division
elif operation == "//":
    print("Result:",num1 // num2  )
# Maximum Value
elif operation == "max":
    print("Result",max(num1,num2)) 
# Minumum Value
elif operation == "min":
    print("Result",min(num1,num2))    
 # Average
elif operation == "avg":
       print("Result:", (num1 + num2) / 2)
# Invalid Operation
else:
    print("Invalid operation")

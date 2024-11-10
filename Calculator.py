print('''Symbols/ Details for operation to perform:
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
// for Floor Division
% for either Percentage (p) or Remainder (r)
square for Square of a number
sqrt for Square Root of a number
cube for Cube of a number
cbrt for Cube Root of a number
! for Factorial of a number
power for Exponentiation or Power Calculation
prime for checking if the number is Prime
reciprocal for Reciprocal of the number
GCD for Greatest Common Divisor
LCM for Least Common Multiple
''')
num1 = float(input("Enter the first number: "))
operator = input("Enter the operation to perform:").strip().lower()

operator_loop = ['sqrt','square','cube','cbrt','!','prime','reciprocal']

if operator not in operator_loop:
    num2 = float(input("Enter the second number: "))
    
    #Addition
    if operator == "+":
        result = num1 + num2
        print(f"{num1} {operator} {num2} = {result}")
    
    #Subtraction
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} {operator} {num2} = {result}")
    
    #Multiplication
    elif operator == "*":
        result = num1 * num2
        print(f"{num1}{operator}{num2} = {result}")
    
    #Division
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "undefined"
        print(f"{num1}{operator}{num2} = {result}")
    
    #Floor Division
    elif operator == "//":
        if num2 != 0:
            result = num1 // num2
        else:
            result = "undefined"
        print(f"The quotient of {num1} divided by {num2} is {result}")
    
    #Percentage (p) Or Remainder (r)
    elif operator == "%":
        percent_or_remainder = input("Do you mean 'percentage' or 'remainder'? Enter 'p' for percentage or 'r' for remainder: ").strip().lower()
        if percent_or_remainder == 'p':
            result = (num1 / num2)*100
            print(f"{num1} as percentage of {num2} is {result}")
        elif percent_or_remainder == 'r':
            result = num1 % num2
            print(f"The remainder of {num1} divided by {num2} is {result}")
        else:
            print("Invalid choice. Please enter 'p' for percentage or 'r' for remainder.")
    
    #Exponentiation or Power
    elif operator == "power":
        result = num1 ** num2
        print(f"{num1} to the power {num2} is {result}")

    #GCD
    elif operator == "gcd":
        a, b = num1, num2
        while b:
            a, b = b, a % b
        print(f"The GCD of numbers {num1} and {num2} is {a}")

    #LCM
    elif operator == "lcm":
        a, b = num1, num2
        while b:
            a, b = b, a % b
        gcd = a
        LCM = abs(num1*num2)//gcd
        print(f"The LCM of numbers {num1} and {num2} is {LCM}")
    
    #Invalid Operators
    else:
        print("Invalid operator. Please enter the valid operator.")

#Square Root
elif operator == "sqrt":
    result = num1**0.5
    print(f"The square root of {num1} is {result}")

#Square
elif operator == "square":
    result = num1**2
    print(f"The square of {num1} is {result}")

#Cube
elif operator == "cube":
    result = num1**3
    print(f"The cube of {num1} is {result}")

#Cube Root
elif operator == "cbrt":
    result = round(num1**(1/3))
    print(f"The cube root of {num1} is {result}")

#Factorial
elif operator == "!":
    if num1 < 0 or num1 != int(num1):
        print("Factorial is not defined for non-integer or negative numbers.")
    elif num1 == 0 or num1 == 1:
        print(f"The factorial of {num1} is 1")
    else:
        factorial = 1
        for i in range(1, int(num1 + 1)):
            factorial *= i
        print(f"The factorial of {num1} is {factorial}")

#Prime Number Check
elif operator == "prime":
    if num1 <= 1:
        print(f"{num1} is not a Prime number.")
    elif num1 != int(num1):
        print("Prime check only applies to whole numbers.")
    else:
        isPrime = True
        for i in range(2, int((num1**0.5)+1)):
            if num1 % i == 0:
                isPrime = False
                break
        if isPrime:
            print(f"{num1} is a Prime number.")
        else:
            print(f"{num1} is not a Prime number.")

#Reciprocal
elif operator == "reciprocal":
    if num1 != 0:
        result = 1 / num1
        print(f"The reciprocal of {num1} is {result}")
    else:
        print(f"The reciprocal of {num1} is not defined")
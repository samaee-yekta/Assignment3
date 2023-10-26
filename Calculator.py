import math
while True:

    op = input("Enter operation (+, -, *, /, sin, cos, tan, cot, factorial, sqrt) or exit: ")
    if op == 'exit':
        break
        
    if op == "+" or op == "-" or op == "*" or op == "/":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
    if op == "+":
            cal = a + b
    if op == "-":
            cal = a - b
    if op == "*":
            cal = a * b
    if op == "/":
        if b == 0:
                cal = "Error"
        else:
                cal = a / b

    if op == "sin" or op == "cos" or op == "tan" or op == "cot" or op == "factorial" or op =="sqrt":
        c = int(input('Enter number: '))
        sin = math.sin
        cos = math.cos
        tan = math.tan
        factorial = math.factorial
        sqrt = math.sqrt
        rd = math.radians

        if op == "sin":
            cal = (sin(rd(c)))
        if op == "cos":
            cal = (cos(rd(c)))
        if op == "tan":
            cal = (tan(rd(c)))
        if op == "cot":
            cal = (1)/(tan(rd(c)))
        if op == "factorial":
            if c < 0:
                cal = "Error"
            else:
                cal = factorial(c)
        if op == "sqrt":
            cal = sqrt(c)

    print(cal)
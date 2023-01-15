response = (input ("do you want it in int or float form?"))
if response == "float":
    num1 = float (input ("Enter first number "))
    op = input ("Enter operation ")
    num2 = float (input ("Enter second number "))

    if op == "+":
        print (num1 + num2)
    elif op == "-":
        print (num1 - num2)
    elif op == "*":
        print (num1 * num2)
    elif op == "/":
        print (num1 / num2)

elif response == "int":
    num1 = int (input ("Enter first number "))
    op = input ("Enter operation ")
    num2 = int (input ("Enter second number "))
    print (type (num2))
    if op == "+":
        print (num1 + num2)
    elif op == "-":
        print (num1 - num2)
    elif op == "*":
        print (num1 * num2)
    elif op == "/":
        print (num1 / num2)


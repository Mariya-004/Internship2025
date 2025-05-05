def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error! Division by zero."
    return a/b
def calculator(op):
    if "+" in op:
        s=op.split("+")
        a=float(s[0])
        b=float(s[1])
        return addition(a,b)
    elif "-" in op:
        s=op.split("-")
        a=float(s[0])
        b=float(s[1])
        return subtraction(a,b)
    elif "*" in op:
        s=op.split("*")
        a=float(s[0])
        b=float(s[1])
        return multiplication(a,b)
    elif "/" in op:
        s=op.split("/")
        a=float(s[0])
        b=float(s[1])
        return division(a,b)
    else:
        return "Invalid operation!"
    
while True:
    op=input("Enter the operation (3+2, 3-2, 3*2, 3/2)etc :")
    result=calculator(op)
    print("Result:",result)
    cont=input("Continue?(y/n):")
    if cont=="n" or cont=="N":
        break
    elif cont=="y" or cont=="Y":
        continue

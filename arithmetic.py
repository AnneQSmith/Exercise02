
#TODO:  Modify add, multiply to accept an arbirary number of arguments
# 

def add(*args):
    print args
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return (sum)

def subtract(num1, num2):
    return(num1-num2)

def multiply(*args):
    print args
    prod = 1
    for i in range(len(args)):
        prod *= args[i]
    return(prod)

def divide(num1, num2):
    fl_num1 = float(num1)
    print fl_num1
    fl_num2 = float(num2)
    print fl_num2
    if fl_num2 != 0.0: 
        return(fl_num1/fl_num2)
    else:
        print("Even you can not divide by zero")
        return 0.0

def square(num1):
    return (num1**2)

def cube(num1):
    return (num1**3)

def power(num1, num2):
    return(num1**num2)

def mod(num1, num2):
    return num1%num2

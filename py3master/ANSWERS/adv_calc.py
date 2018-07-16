#!/usr/bin/env python

def is_valid_number(num_string):
    is_num = num_string.strip().replace('.', '').isdigit()
    return is_num

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return float('Nan')
    else:
        return x/y

def exp(x,y):
    return x ** y

def mod(x,y):
    if y == 0:
        return float('Nan')
    else:
        return x%y

while True:
    expr = input("Enter a math expression: ")

    if expr.lower() == 'q':
        break

    (v1, op, v2) = expr.split()
    if is_valid_number(v1) and is_valid_number(v2):
        v1 = float(v1)
        v2 = float(v2)
    else:
        print("Sorry, invalid input")
        continue

    if op == '+':
        result = add(v1,v2)
    elif op == '-':
        result = sub(v1,v2)
    elif op == '*':
        result = mul(v1,v2)
    elif op == '/':
        result = div(v1,v2)
    elif op == '**':
        result = exp(v1,v2)
    elif op == '%':
        result = mod(v1,v2)
    else:
        print("Bad operator!")
        continue

    print("{0:.3f}".format(result))


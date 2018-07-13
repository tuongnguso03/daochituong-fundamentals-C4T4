from random import *

def generate_quiz():
    x = randint(0,10)
    operation = choice(["+","-","*","/"])
    y = randint(0,10)
    error=choice([-2,-1,0,0,0,0,1,2])

    if operation == "+":
        res = x+y
    elif operation == "-":
        res= x - y
    elif operation == "*":
        res= x*y
    elif operation == "/":
        if y!=0:
            res= x/y
        else:
            res=x+y
            operation="+"
            
    result=res+error    
    return [x, y, operation, result]

def check_answer(x, y, op, result, user_choice):
    if op == "+":
        res = x+y
    elif op == "-":
        res= x - y
    elif op == "*":
        res= x*y
    elif op == "/":
        res= x/y 

    if result == res:
        true_choice=True
    else:
        true_choice=False    

    return bool(true_choice == user_choice)

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:57:01 2020

@author: User
"""

import ast,operator,sys




def calculator3():
    
    def ex():
        q_a = input('Do you want more calculations? (Y/N))? ')
        q_a = q_a.capitalize()
        if q_a == 'Y':
            calculator3()
        elif q_a == 'N':
            print('Exit. ')        
            sys.exit

        else:
            ex()
    
    operators = {ast.Add: operator.add, ast.Sub: operator.sub,
                 ast.Mult: operator.mul, ast.Div: operator.truediv,
                 ast.Mod: operator.mod,}
    
    def error():
        print('Error. Try again?')
        answer = input('Y/N ')
        answer = answer.capitalize()
        if answer == 'Y':
            calculator3()
        elif answer == 'N':     
            sys.exit
            
            
    string = input('Ask me anything: ')
    try:
        node = ast.parse(string, mode='eval')
    except ValueError:
        error()


    def calculator3_1(node):
        try:
            if isinstance(node, ast.Expression):
                return calculator3_1(node.body)
            elif isinstance(node, ast.Str):
                return node.string
            elif isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.BinOp):
                return operators[type(node.op)](calculator3_1(node.left),\
                             calculator3_1(node.right))
            else:
                error()
        except ZeroDivisionError:
            print('ZeroDivisionError')
        except ValueError:
            sys.exit
            

    try:
        calculator3_1(node.body)
    except ValueError:
        error()
    except UnboundLocalError:
        error()

        
xx = calculator3()

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:26:52 2020

@author: User
"""


import ast,operator,sys

        
        
def calculator1():
    def ex():
        q_a = input('Do you want more calculations? (Y/N))? ')
        q_a = q_a.capitalize()
        if q_a == 'Y':
            calculator1()
        elif q_a == 'N':
            print('Exit. ')        
            sys.exit
        else:
            ex()  
    
    
    def error():
        print('Error. Try again?')
        answer = input('Y/N ')
        answer = answer.capitalize()
        if answer == 'Y':
            calculator1()
        elif answer == 'N':
            print('Exit. ')        
            sys.exit    
    op = ['+','-','*','/']
    
    a = input('First number: ')
    try:
        a = float(a)
    except ValueError as e:
        error()    
    else:
        b = input('Second number: ')
        try:
            b = float(b)
        except ValueError as e:
            error()
        else:
            c = input('Opertor (+, -, *, /): ')
            try:
                c in op
            except ValueError as e:
                error()
            else:
                if c == '+':
                    print(round((a + b),2))
                elif c == '-':
                    print(round((a - b),2))
                elif c == '*':
                    print(round((a * b),2))
                elif c == '/':
                    try:
                        print(round((a / b),2))
                    except ZeroDivisionError:
                        print('ZeroDivisionError')

                ex() 



'''
-----------------------------------------------------------------------------
'''



def calculator2():
    def ex():
        q_a = input('Do you want more calculations? (Y/N))? ')
        q_a = q_a.capitalize()
        if q_a == 'Y':
            calculator2()
        elif q_a == 'N':
            print('Exit. ')        
            sys.exit
        else:
            ex()  
    
    
    def error():
        print('Error. Try again?')
        answer = input('Y/N ')
        answer = answer.capitalize()
        if answer == 'Y':
            calculator2()
        elif answer == 'N':     
            sys.exit
    
    srting = input('Enter count elements: ')
    operator = ['*', '/', '+', '-']
    
    try:
        integer = int(srting)
    except ValueError as e:
        error()

    else:
        integer = int(srting)
        if integer == 1:
            error()
    
    full = []
    for i in range(integer + (integer - 1)):
            
        if i % 2 == 0:
            i = input('Enter var{}: '.format(int(i/2 + 1)))
            try:
                full.append(float(i))
            except ValueError:
                error()
        else:
            i = input('Enter operation{}: '.format(int(i/2 + 1))) 
            if i not in operator:
                error()
            else:
                full.append(i)   

    
    
    
    def calculator2_1(full:list):
        
        full_1 = full.copy()

        if len(full_1) > 3:
            
            if len(full_1) > 3:    
                for j in range(len(full_1)):
                    if full_1[j] == '*':
                        full_1[j-1] *= full_1.pop(j+1)
                        full_1.remove(full_1[j])
                        return calculator2_1(full_1)
                    elif full_1[j] == '/':
                        full_1[j-1] /= full_1.pop(j+1)
                        full_1.pop(j)
                        return calculator2_1(full_1)    
            else:
                return full_1
            
            if len(full_1) > 3:
                for jj in range(len(full_1)):
                    if full_1[jj] == '+':
                        full_1[jj-1] += full_1.pop(jj+1)
                        full_1.remove(full_1[jj])
                        return calculator2_1(full_1)
                    elif full_1[jj] == '-':
                        full_1[jj-1] -= full_1.pop(jj+1)
                        full_1.pop(j)
                        return calculator2_1(full_1)
            else:
                return full_1
        else:
            for k in range(len(full_1)):
                if full_1[k] == '*':
                    full_1[k-1] *= full_1.pop(k+1)
                    full_1.remove(full_1[k])
                    return full_1
                elif full_1[k] == '/':
                    full_1[k-1] /= full_1.pop(k+1)
                    full_1.pop(k)
                    return full_1
                elif full_1[k] == '+':
                    full_1[k-1] += full_1.pop(k+1)
                    full_1.remove(full_1[k])
                    return full_1
                elif full_1[k] == '-':
                    full_1[k-1] -= full_1.pop(k+1)
                    full_1.pop(k)
                    return full_1


    solution = calculator2_1(full)

    print('Answer: {}'.format(solution[0]))
    return solution, ex()
#    
#try:
#    answer = calculator2()
#except TypeError:
#    error()



'''
-----------------------------------------------------------------------------
'''



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
#                raise Exception('ValueError')

        except ZeroDivisionError:
            print('ZeroDivisionError')
        except ValueError:
            error()
#        except ValueError:
#            error()
            

    try:
        calculator3_1(node.body)
    except ValueError:
        print('-')
#        error()
    except UnboundLocalError:
        print('--')
#        error()
    else:
        print(calculator3_1(node.body))
        ex()
#        return calculator3_1(node.body)



print('Welcome to calculation system 2000!')


    
def main():
    print('''
  Please, choose your assistant:
    1 - Cleaner
    2 - Student
    3 - Expert\n''')
    temp = int(input('Enter number 1,2,3: '))
    if temp == 1:
        calculator1()
    elif temp == 2:
        calculator2()
    elif temp == 3:
        calculator3()
    else:
        print('Please, try again.')
        main()
        
main()    

input('Press Enter to exit')
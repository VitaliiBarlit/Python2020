# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:53:13 2020

@author: User
"""


import sys



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
    
try:
    answer = calculator2()
except TypeError:
    error()

















    
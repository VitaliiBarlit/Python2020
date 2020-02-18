# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:02:58 2020

@author: User
"""
import sys

def ex():
    q_a = input('Do you want more calculations? (Y/N))? ')
    q_a = q_a.capitalize()
    if q_a == 'Y':
        calculator1()
    elif q_a == 'N':
        print('Exit. ')        
        sys.exit

#    else:
#        print('Keyword error.')
#        ex()

def error():
    print('Error. Try again?')
    answer = input('Y/N ')
    answer = answer.capitalize()
    if answer == 'Y':
        calculator1()
    elif answer == 'N':
        print('Exit. ')        
        sys.exit
        
        
def calculator1():
    op = ['+','-','*','/']
    
    a = input('First number: ')
    try:
        a = float(a)
    except ValueError as e:
        print('Error')
    
    else:
        b = input('Second number: ')
        try:
            b = float(b)
        except ValueError:
            print('Error')
        else:
            c = input('Opertor (+, -, *, /): ')
                
            while c not in op:
                print('Uknown operation. Try again. ')
                c = input('Opertor (+, -, *, /): ')
            
            if c == '+':
                print(a + b)
            elif c == '-':
                print(a - b)
            elif c == '*':
                print(a * b)
            elif c == '/':
                try:
                    print(a / b)
                except ZeroDivisionError:
                    print('ZeroDivisionError')

    ex() 
                    
calculator1()
                    
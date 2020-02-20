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
      
        
        
def calculator1():
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
                    
calculator1()
                    
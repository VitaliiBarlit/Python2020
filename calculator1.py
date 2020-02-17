# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:02:58 2020

@author: User
"""


def calculator1():
    op = ['+','-','*','/']
    
    a = input('First number: ')
    try:
        a = float(a)
    except ValueError as e:
        print('Error.')
    
    else:
        b = input('Second number: ')
        try:
            b = float(b)
        except ValueError:
            print('Error.')
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
                    
                    
calculator1()
                    
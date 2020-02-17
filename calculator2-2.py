# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:01:23 2020

@author: User
"""

def count():
    while True:
        var_num = input('Enter element count: ')
        try:
            int(var_num)
        except ValueError:
            print('Error')
        else:
            return int(var_num)

#x = count()
#
#def num_type(i:int):
#    a = input('Enter var{} : '.format(i + 1))
#    try:
#        float(a)
#    except ValueError:
#        print('Error.')
#    else:
#        return float(a)
#        
#
#def num_n(n:int,x:list):
#    j = 0
#    while j < n:
#        k = num_type(j)
#        if k is not None:
#            x.append(k)
#            j += 1
#    return x       
#
#def num(x):
#    op = ['+','-','*','/']
#    numbers = []
#    operators = []
#    for i in range(x):
#        for j in range(x-1):
#
#            
#
#            m = input('Enter var{}: '.format(i + 1))
#            try:
#                float(m)
#            except ValueError:
#                print('Error.')
#            else:
#                k = num_n(j,numbers)
#                if k is not None:                
#                    numbers.append(float(m))
#
#            n = input('Enter operator{}: '.format(j + 1))
##            while n not in op:
##                print('Uknown operation. Try again. ')
##                n = input('Opertor (+, -, *, /): ')       
#    print(numbers)
#y = num(x)
            
        
        
        
        
        
        
        
        
        
        
        
        
n_n = []
m_m  = []
        
for i in range(3):
    m = int(input('{}: '.format(i + 1)))
    m_m.append(m)
    for j in range(2):
        n = int(input('{}: '.format(j + 1)))
        n_n.append(n)
        
        
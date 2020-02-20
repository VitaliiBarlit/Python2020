# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:03:57 2020

@author: User
"""


#var_num = input('Enter element count: ')
#op_num = 0
#try:
#    var_num = int(var_num)
#except ValueError:
#    print('Error')
#else:
#    num_op = var_num - 1
    
#lst_var = []    
#lst_op = []
#for i in range(var_num):
#    i = input('Enter var{}: '.format(i+1))
#    lst_var.append(i)
#    
#for j in range(op_num):
#    j = input('Enter var{}: '.format(j+1))
#    lst_op.append(j)
#    
    

def num_type(i:int):
    a = input('Enter var{} : '.format(i + 1))
    try:
        float(a)
    except ValueError:
        print('Error.')
    else:
        return float(a)
        

def num_n(n:int,x:list):
    j = 0
    while j < n:
        k = num_type(j)
        if k is not None:
            x.append(k)
            j += 1
    return x       


def op_num():
    op = ['+','-','*','/']
#    op.append(dir(math)[5:])
    c = input('Opertor (+, -, *, /): ')
        
    while c not in op:
        print('Uknown operation. Try again. ')
        c = input('Opertor (+, -, *, /): ')
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:01:23 2020

@author: User
"""

import operator as op

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

#try:
#    op.add('a',2)
#except TypeError:
#    print('Error')
#    try:
#        a = input('Enter correct value: ') 
#        a = int(a)
#    except ValueError:
#        print('Error')
#        a = input('Enter correct value: ')
#    else:
#        print(op.add(a,2))
#sl = []
#n = int(input())
#nums = []
#for k in range(n):
#    nums.append(str())
#print(nums)
#
#s = input('Enter: ')
#first = str()
#for _ in s:
#    sl.append(_)
#
#for j in sl:
#    if j.isdigit() == True:
#        

#import re

#s = re.findall()

#n = input('Enter: ')
#n = n.replace('*','x')
#m = re.findall(r"([\d.]*\d+)", n)
#o = re.findall(r"\+|-|/|x",n)
#



x=[]
amount=int(input("How many numbers?"))
operation=input("(*), (/), (+), (-)")
previous1 = 0
previous2=1
for i in range(amount):
    number=int(input("Number: "))
    x.append(number)
if operation == "+":
    for i in range(amount):
        previous1=x[i]+previous1
elif operation == "*":
    for i in range(amount):
        previous2=x[i]*previous2
elif operation == "-":
    for i in range(amount):
        previous1=x[i]-previous1
elif operation == "/":
    for i in range(amount):
        previous2=x[i]/previous2
if operation == "+" or operation == "-":
    print(previous1)
else:
    print(previous2)
    
    










































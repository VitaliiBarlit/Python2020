# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:53:13 2020

@author: User
"""

#x = []
#y = []
#amount = int(input('How many numbers? '))
#operation = input('(*), (/), (+), (-)')
#previous1 = 0
#previous2 = 1
#for i in range(amount):
#    number=int(input('Number: '))
#    
#    x.append(number)
#    y.append('')
#
#
#if operator == '*':
#    n = y.index('*')
#    print(x[n])
#
#if operation == '+':
#    for i in range(amount):
#        previous1=x[i]+previous1
#elif operation == '*':
#    for i in range(amount):
#        previous2=x[i]*previous2
#elif operation == '-':
#    for i in range(amount):
#        previous1=x[i]-previous1
#elif operation == '/':
#    for i in range(amount):
#        previous2=x[i]/previous2
#if operation == '+' or operation == '-':
#    print(previous1)
#else:
#    print(previous2)

#x = count()

srting = input('Enter count elements: ')

try:
    integer = int(srting)
except ValueError as e:
    print('Err')
else:
    integer = int(srting)
    if integer == 1:
        print('Error')
        
var = []
op = []
full = []
for i in range(integer + (integer - 1)):
    if i % 2 == 0:
        i = int(input('Enter var{}: '.format(int(i/2 + 1))))
#        var.append(i)
        full.append(i)
    else:
        i = input('Enter operation: ')
#        op.append(i)
        full.append(i)        

#for j in range(len(full)): 
#    if full[j] == '*' or '/':
#        if full[j] == '*':
#            full[j-1] *= full[j+1]
#            full.remove(full.index(full[j+1]))
#            print(full)
#            var[full[j-1]] *= var[full[j+1]]
#            print(full[j])
#            var.remove(var[full[j+1]])
#            print(var)
#        elif full[j] == '/':
#            var[op.index(op[j])] /= var[op.index(op[j])+1]
#            var.remove(var[op.index(op[j])+1])
#            print(var)
#    if full[j] == '+' or '-':
#        if full[j] == '+': 
#            var[op.index(op[j])] *= var[op.index(op[j])+1]
#            print(op.index(op[j]))
#            var.remove(var[op.index(op[j])+1])
#            print(var)
#        elif full[j] == '-':
#            var[op.index(op[j])] /= var[op.index(op[j])+1]
#            var.remove(var[op.index(op[j])+1])
#            print(var)           
            
            
            
#for k in range(len(op)): 
#    if op[k] == '+' or '-':
#        if op[k] == '+': 
#            var[op.index(op[k])] *= var[op.index(op[k])+1]
#            print(op.index(op[j]))
#            var.remove(var[op.index(op[k])+1])
#            print(var)
#        elif op[k] == '-':
#            var[op.index(op[k])] /= var[op.index(op[k])+1]
#            var.remove(var[op.index(op[k])+1])
#            print(var)





def calc1(full:list):
    
    full_1 = full.copy()
        
        
    for j in range(len(full)):
    #        while full[j] == '*' or '/':
        if full[j] == '*' or '/':
            if full[j] == '*':
                temp = full_1.pop(j+1)
                full_1[j-1] *= temp
                full_1.remove(full[j])
                print(full_1)
                return calc1(full_1)
            elif full[j] == '/':
                temp = full_1.pop(j+1)
                full_1[j-1] /= temp
                full_1.pop(j)
                return calc1(full_1)
        else:
            print(full_1)
            return full_1
        
answer = calc1(full)
#full_1 = calc1(full)
#print(full_1)
            
            
            
#full_2 = full_1.copy()  

          
#for j in range(len(full_1)):
#    if full_1[j] == '+' or '-':
#        if full_1[j] == '+':
#            temp = full_2.pop(j+1)
#            full_2[j-1] += temp
#            full_2.pop(j)
#        elif full_1[j] == '-':
#            temp = full_2.pop(j+1)
#            full_2[j-1] -= temp
#            full_2.pop(j)
#
#
#
#print('Answer: {}'.format(full_2[0]))




















    
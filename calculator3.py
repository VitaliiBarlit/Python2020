# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:57:01 2020

@author: User
"""

import ast, operator

binOps = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod
}

def calculator3():
    s = input('Ask me anything: ')
    node = ast.parse(s, mode='eval')

    def calculator3_1(node): # isinstance(var,Type) <=> type(var) = Type
        if isinstance(node, ast.Expression):
            return calculator3_1(node.body)
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return binOps[type(node.op)](calculator3_1(node.left),\
                         calculator3_1(node.right))
        else:
            raise Exception('ValueError')

            calculator3()
    return calculator3_1(node.body)

x = calculator3()
print(x)
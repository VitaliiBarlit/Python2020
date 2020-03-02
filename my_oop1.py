# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:44:25 2020

@author: User
"""

class Warrior():
    
    def __init__(self, name, clss, hp, sp, weapon,damage):
        self.name = name
        self.clss = clss
        self.hp = hp
        self.sp = sp
        self.weapon = weapon
        self.damage = damage
        
    def __doc__(self):
        print('You create warrior by name {}. He is {} and armed with {}.'\
              .format(self.name, self.clss, self.weapon))
#    def intro(self):
#        print('Name is {}'.format(self.name))
         
    def setHP(self, hp):
        self.hp = hp
        return self.hp   
    def gethp(self):
        return self.hp
    
#    def smash(self,damage,health):
#        self.health = health - damage
#        return Warrior.setHP(self,health)    
    
    def fireball(self,hp,damage):
        return Warrior.setHP(self,hp-damage)
            
W1 = Warrior('Orc', 'Barbarian', 500, 100, 'Axe',75)
W2 = Warrior('Vexillor', 'Knight', 500, 100, 'Great Sword',50)

#print(W2.fireball(W1.hp,W2.damage))
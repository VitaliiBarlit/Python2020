# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:24:05 2020

@author: User
"""

class Terrain:
    def __init__(self, name, feature):
        self.name = name
        self.feature = feature
#        print('{} is {}.'.format(self.name,self.feature))

class Build(Terrain):
    def __init__(self, name, feature, area, height):
        super().__init__(name,feature)
        self.height = height
        self.residents = True
    def no_residents(self):
        self.residents = False

class Creatures(Terrain):
    def __init__(self, name, feature, num_of_people, residence):
        super().__init__(name,feature)
        self.num_of_people = num_of_people
        self.residence = residence
    def info(self):
        if self.num_of_people == 1:
            return '{} live in {}'.format(self.name, self.residence.lower())
        else:
            return '{} {} live in {}'.format(self.num_of_people, \
                self.name.lower(), self.residence.lower())
        
        
hill = Terrain('Hill', 'High')
moat = Terrain('Moat', 'Deep')

wall = Build('Fortress wall','Grey','Around',100)
gate = Build('Gate','Grey','Rectangle',90)
gate.no_residents()

keep = Build('Keep', 'High', 'Square', 250)
palace = Build('Palace', 'Great building', 'Old cacstle', 200)

archers = Creatures('Archers', 'With bow', 20, keep.name)
king = Creatures('King', 'With scepter', 1, palace.name)
king_info= king.info() + ' with his family and servants.'


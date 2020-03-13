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

class Build:
    def __init__(self, name, top_view, height):
        self.name = name
        self.top_view = top_view
        self.height = height
        self.residents = True
    def no_residents(self):
        self.residents = False

class People:
    def __init__(self, name, num_of_people, residence):
        self.name = name
        self.num_of_people = num_of_people
        self.residence = residence
    def __str__(self):
#        return '{} live in {}'.format(self.name, self.residence.lower())
        if self.num_of_people == 1:
            return '{} live in {}'.format(self.name, self.residence.lower())
        else:
            return '{} {} live in {}'.format(self.num_of_people, \
                self.name.lower(), self.residence.lower())
        
        


        
hill = Terrain('Hill', 'High')
moat = Terrain('Moat', 'Deep')

wall = Build('Great wall', 'Ring', 150)
gate = Build('Steel gate', 'Rectangle', 175)
outbuildings = Build('Happy outbuildings', 'Boxes', 50)
keep = Build('High tower', 'Square', 225)
courtyard = Build('Green courtyard', 'Circle', 0)
palace = Build('Royal palace', 'Old castle', 200)

#king = People('King', 1, palace.name)

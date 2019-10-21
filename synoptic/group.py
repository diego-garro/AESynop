#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Package: group.py
versión: 0.0.1

Este es un módulo para las herramientas referentes al análisis y evaluación de los reportes
sinópticos. En específico este módulo contiene la definición de un grupo del reporte y su
estructura. Se establecen sus características por medio de una clase.
"""

class Group(object):

    def __init__(self, group, group_name=''):
        self.group = group
        self.name = group_name
        self.len = len(group)
    
    def less_than_five_digits(self):
        return("The group {} has less than five digits.".format(self.name))
    
    def more_than_five_digits(self):
        return("The group {} has more than five digits.".format(self.name))
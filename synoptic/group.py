#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Package: group.py
versión: 0.0.1

Este es un módulo para las herramientas referentes al análisis y evaluación de los reportes
sinópticos. En específico este módulo contiene la definición de un grupo del reporte y su
estructura. Se establecen sus características por medio de una clase.

Modo: from .group import Group
"""

class Group(object):
    """
    Clase que defina la base de un grupo perteneciente a cualquier reporte sinóptico.
    """

    def __init__(self, group, group_name=''):
        self.group = group
        self.name = group_name
        self.len = len(group)
    
    def less_than_five_digits(self):
        return("The group {} has less than five digits.".format(self.name))
    
    def more_than_five_digits(self):
        return("The group {} has more than five digits.".format(self.name))
    
    def verify_group_indicator(self, value, digits=1):
        if self.group[0:digits] != value:
            return False
        return True
    
    def verify_indicator(self, indicator, range_list):
        if indicator in range_list:
            return True
        return False
    
    def extract_indicator(self, init_index, end_index):
        return self.group[init_index:end_index]
#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Package: group.py
versión: 0.0.1

This module contains the class that defines the structure of
a five-digit group present within the synoptic report.

Mod: from .group import Group
"""

class Group(object):
    """
    Class that defines the basis of a group belonging to any synoptic report.
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

class Type_ABCDD(Group):
    """
    Class to define type ABCDD of groups.
    """

    def __init__(self, group, file_error='', synop_type='main'):
        Group.__init__(self, group)
        self.file = file_error
        self.synop_type = synop_type
    
    def extract_indicators(self):
        self.A = self.extract_indicator(0, 1)
        self.B = self.extract_indicator(1, 2)
        self.C = self.extract_indicator(2, 3)
        self.DD = self.extract_indicator(3, 5)
    


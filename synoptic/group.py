#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Package: group.py
versión: 0.0.1

This module contains the class that defines the structure of
a five-digit group present within the synoptic report.

Mod: from .group import Group
"""

__author__ = "Diego Antonio Garro Molina"
__copyright__ = "Copyright 2018, Diego Garro e Instituto Meteorológico Nacional"
__credits__ = "Diego Garro, Instituto Meteorologico Nacional"
__license__ = "None"
__version__ = "1.0.0"
__maintaier__ = "Diego Garro Molina"
__email__ = "dgarro@imn.ac.cr"
__status__ = "Developer"

class Group(object):
    """
    Class that defines the basis of a group belonging to any synoptic report.
    """

    def __init__(self, group, group_name=''):
        self.group = group
        self.name = group_name
        self.n_digits = len(group)
    
    def less_than_five_digits(self):
        print("The group {} has less than five digits.".format(self.name))
    
    def more_than_five_digits(self):
        print("The group {} has more than five digits.".format(self.name))
    
    def evaluate_length(self):
        if self.n_digits < 5:
            self.less_than_five_digits()
            return '<5'
        elif self.n_digits > 5:
            self.more_than_five_digits()
            return '>5'
        else:
            return '=5'
     
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

    errors = {1 : ''}

    def __init__(self, group, file_error='', synop_type='main'):
        Group.__init__(self, group)
        self.f = file_error
        self.synop_type = synop_type
        self.group_length = self.evaluate_length()
        self.extract_indicators()
    
    def extract_indicators(self):
        self.A = self.extract_indicator(0, 1)
        self.B = self.extract_indicator(1, 2)
        self.C = self.extract_indicator(2, 3)
        self.DD = self.extract_indicator(3, 5)

	def evaluate_identifier(self, comparator, err_key):
		if self.A.isdigit():
			self.A = int(self.A)
			if self.A == comparator:
				self.group_id = True
			else:
				self.group_id = False
		else:
			print(self.errors[err_key])
			self.f.write(self.errors[err_key] + '\n')
			self.group_id = True

    def evaluate_group(self):
        pass

    


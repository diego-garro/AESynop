#!/usr/bin/python3
#-*-coding: utf-8-*

"""
This module performs an exhaustive review of section 1 of the synoptic report.

This section is standard for all stations transmitting synoptic reports.

MiMiMjMj YYGGiw - Bulletin Header and Date/Time Group

As the reports are collected from various stations they are reformatted (by computer) into
bulletins, with each bulletin containing reports from specific stations. The above two groups will
be included only as the first line of the text, the bulletin header. The bulletin following contains
only land station SYNOP reports which were taken at the same time and which use the same units
for reporting wind speed.
"""

__author__ = "Diego Antonio Garro Molina"
__copyright__ = "Copyright 2018, Diego Garro e Instituto Meteorológico Nacional"
__credits__ = "Diego Garro, Instituto Meteorologico Nacional"
__license__ = "None"
__version__ = "1.0.0"
__maintaier__ = "Diego Garro Molina"
__email__ = "dgarro@imn.ac.cr"
__status__ = "Developer"

from .group import Type_ABCDD

class Group_iRixhVV(Type_ABCDD):

    errors = {
        1 : "\tERROR IN SECTION 1: Indicator iR for inclusion or omission of precipitation data it is not a number.",
		2 : "\tERROR IN SECTION 1: Indicator iR for inclusion or omission of precipitation data it is not in Table 1819.",
		3 : "\tERROR IN SECTION 1: Indicator ix for type of station operation and for present and past weather data it is not a number.",
		4 : "\tERROR IN SECTION 1: Indicator ix for type of station operation and for present and past weather data it is not in Table 1860.",
		5 : "\tERROR IN SECTION 1: Indicator h for height above surface of the base of the lowest cloud seen it is not a number.",
		6 : "\tERROR IN SECTION 1: Indicator h for height above surface of the base of the lowest cloud seen it is not in Table 1600.",
		7 : "\tERROR IN SECTION 1: Indicator VV for horizontal visibility at the surface it is not in Table 4377.",
		8 : "\tERROR IN SECTION 1: Indicator VV for horizontal visibility at the surface it is not a number.",
		9 : "\tERROR IN SECTION 1: Group iRixhVV has more than five digits.",
		10 : "\tERROR IN SECTION 1: Group iRixhVV has less than five digits.",
		11 : "\tERROR IN SECTION 1: Indicator iR it is not coded as 0 or 1 in intermediate standard times reports."
    }

    def __init__(self, group, file_error='', synop_type='main'):
        Type_ABCDD.__init__(self, group, file_error=file_error, synop_type=synop_type)
        self.iR = self.A
        self.ix = self.B
        self.h = self.C
        self.VV = self.DD
    
	def evaluate_iR(self):
		if self.iR.isdigit():
			self.iR = int(self.iR)
			if self.synop_type == 'no main':
				if self.iR == 0 or self.iR == 1:
					print(self.errors[11])
					self.f.write(self.errors[11] + '\n')
			try:
				print("Precipitation preceding the observation:",self.table_1819[self.iR])
			except KeyError:
				print(self.errors[2])
				self.f.write(self.errors[2] + '\n')
		else:
			print(self.errors[1])
			sefl.f.write(self.errors[1] + '\n')
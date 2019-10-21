#!/usr/bin/python3
#-*-coding: utf-8-*

"""
This module contains code tables for section one of synoptic report.
"""

__author__ = "Diego Antonio Garro Molina"
__copyright__ = "Copyright 2018, Diego Garro e Instituto Meteorológico Nacional"
__credits__ = "Diego Garro, Instituto Meteorologico Nacional"
__license__ = "None"
__version__ = "1.0.0"
__maintaier__ = "Diego Garro Molina"
__email__ = "dgarro@imn.ac.cr"
__status__ = "Developer"

TABLE_1819 = {
    0 : "Sections 1 and 3, included in both sections.",
	1 : "Section 1 included.",
	2 : "Section 3 included.",
	3 : "In neither section 1 or 3, omitted (precipitation amount = 0).",
	4 : "In neither section 1 or 3, omitted (precipitation amount not available)."
}
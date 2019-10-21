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

    
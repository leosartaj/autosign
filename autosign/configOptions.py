#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

"""
Contains Various Config Options
"""

__rc__ = '.signrc' # default rc name

# defult options for a section
DEFAULT_OPTIONS = {'ext': '.py', 'start': '##', 'line': '#', 'end': '##', 'blank': 'True'}

SPECIAL_OPTIONS = {'allow': '^#!.*python.*$'}

class options:
    """
    Special class for storing options
    """
    def __init__(self, options_dic):
        pass

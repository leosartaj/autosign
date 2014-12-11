#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

"""
Contains various exceptions
"""

class TemplateError(Exception):
    """
    Raise when there is an error with the Template
    """
    pass

class UnsignedError(Exception):
    """
    Raise when file is unsigned, and sign is required
    for the operation
    """
    pass

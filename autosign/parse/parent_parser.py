#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

"""
Contains helper functions for parsing arguments
"""

import argparse # parsing the options

try:
    from autosign import __desc__ # try to get version number
except ImportError:
    __desc__ = 'UNKNOWN'

def gen_parent_parser():
    """
    Parses the arguments
    """
    parser = argparse.ArgumentParser(add_help=False, conflict_handler='resolve')

    help = "Current version of autosign"
    parser.add_argument('--version', '-v',  action='version', help=help, version=__desc__)

    help = "For Verbose Output."
    parser.add_argument('--verbose', '-v',  action='store_true', help=help, dest='verbose')

    help = "For recursive operation. Defaults to False"
    parser.add_argument('--recursive', '-r',  action='store_true', help=help, dest='recursive')

    help = "Generate a basic rc."
    parser.add_argument('--init', action='store_true', help=help, dest='init')

    help = "Location of signrc."
    parser.add_argument('--signrc', help=help, default=None, dest='signrc')

    return parser

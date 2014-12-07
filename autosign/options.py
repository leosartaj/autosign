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
import os

try:
    from autosign import __desc__ # try to get version number
except ImportError:
    __desc__ = 'UNKNOWN'

def parse_args():
    """
    Parses the arguments
    """
    parser = argparse.ArgumentParser(description='Autosign python files quickly')

    help = "Current version of autosign"
    parser.add_argument('--version', '-v',  action='version', help=help, version=__desc__)

    help = "For recursive operation. Defaults to False"
    parser.add_argument('--recursive', '-r',  action='store_true', help=help, dest='recursive')

    sign_group = parser.add_argument_group('sign')

    help = "The location of the signature template."
    sign_group.add_argument('signfile', type=str, help=help)

    help = "The target to be signed with the template."
    sign_group.add_argument('target', type=str, help=help)

    help = "If signature of signed files should be replaced. Defaults to False"
    sign_group.add_argument('--force', '-f',  action='store_true', help=help, dest='force')

    args = parser.parse_args()

    return args

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

    help = "The location of the signature template."
    parser.add_argument('signfile', type=str, help=help)

    help = "The target to be signed with the template."
    parser.add_argument('target', type=str, help=help)

    help = "Current version of autosign"
    parser.add_argument('--version', '-v',  action='version', help=help, version=__desc__)

    help = "For recursive signature addition. Defaults to True"
    parser.add_argument('--recursive', '-r',  action='store_true', help=help, dest='recursive')

    help = "If signature of signed files should be replaced. Defaults to False"
    parser.add_argument('--force', '-f',  action='store_true', help=help, dest='force')

    args = parser.parse_args()

    return args

"""
Contains helper functions for parsing arguments
"""

import optparse # parsing the options
import os

try:
    from signature import __desc__ # try to get version number
except ImportError:
    __desc__ = 'UNKNOWN'

def parse_args():
    """
    Parses the arguments
    """
    usage = """
"""
    parser = optparse.OptionParser(usage, version=__desc__)

    help = "For verbose output. Defaults to False"
    parser.add_option('--verbose', '-v', action='store_true', help=help, dest='verbose')

    help = "For recursive signature addition. Defaults to True"
    parser.add_option('--recursive', '-r',  action='store_true', help=help, dest='recursive')

    help = "If signature of signed files should be replaced. Defaults to False"
    parser.add_option('--force', '-f',  action='store_true', help=help, dest='force')

    options, args = parser.parse_args()

    if len(args) != 2 and len(args) != 3:
        parser.error('Expecting 2, got ' + str(len(args)) + ' argument(s)')

    return options, args

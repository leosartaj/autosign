"""
Contains helper functions for parsing arguments
"""

import optparse # parsing the options

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

    help = "For verbose output"
    parser.add_option('--verbose', '-v', action='store_true', help=help, dest='verbose')

    help = "For recursive signature addition"
    parser.add_option('--recursive', '-r',  action='store_true', help=help, dest='recursive')

    options, args = parser.parse_args()

    return options, args

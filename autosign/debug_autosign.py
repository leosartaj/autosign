#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

"""
For debugging purposes
debugging version of autosign
"""

import os
import main
from parse.autosign_options import parse_args

def format_signfile(signfile):
    """
    formatting for signfile
    """
    msg = 'Signing using ' + signfile
    return msg

def format(filename):
    """
    Formats for verbose output
    """
    msg = filename + ' has been signed.'
    return msg

def gen_summary(signed, unsigned):
    """
    Generates the stats
    """
    stats = ''
    stats += '\nTotal Scanned Files: ' + str(signed + unsigned)
    stats += '\nSigned Files: ' + str(signed)
    return stats

if __name__ == '__main__':
    args = parse_args()

    signfile = args.signfile
    if not os.path.isfile(signfile):
        raise IOError('file \'%s\' does not exist.' %(signfile))
    target= args.target
    if not os.path.exists(target):
        raise IOError('file/dir \'%s\' does not exist.' %(target))

    if args.verbose:
        print format_signfile(signfile), '\n'

    signed, unsigned = 0, 0
    for filename, val in main.signFiles(signfile, target, args.recursive, args.force):
        if val:
            if args.verbose:
                print format(filename)
            signed += 1
        else:
            unsigned += 1

    if args.verbose:
        print gen_summary(signed, unsigned)

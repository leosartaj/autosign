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
debugging version of listsign
"""

import os
import main
from parse.listsign_options import parse_args

def format(filename, val):
    """
    Formats for verbose output
    """
    if val:
        result = 'signed'
    else:
        result = 'not signed'
    msg = filename + ' is ' + result
    return msg

def gen_summary(signed, unsigned, args):
    """
    Generates the stats
    """
    stats = ''
    if args.verbose:
        stats += '\n'
    stats += 'Total Scanned Files: ' + str(signed + unsigned)
    if args.complete or args.sign:
        stats += '\nSigned Files: ' + str(signed)
    if args.complete or args.usign:
        stats += '\nUnsigned Files: ' + str(unsigned)
    return stats

if __name__ == '__main__':
    args = parse_args()

    target = args.target
    if not os.path.exists(target):
        raise IOError('file/dir \'%s\' does not exist.' %(target))

    if not args.complete and not args.sign and not args.usign:
        args.complete = True

    signed, unsigned = 0, 0
    for filename, val in main.checkFiles(target, args.recursive):
        if val:
            if args.verbose and (args.sign or args.complete):
                print format(filename, val)
            signed += 1
        else:
            if args.verbose and (args.usign or args.complete):
                print format(filename, val)
            unsigned += 1
    print gen_summary(signed, unsigned, args)

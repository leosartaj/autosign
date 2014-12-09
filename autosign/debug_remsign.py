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
debugging version of remsign
"""

import os
import main
from parse.remsign_options import parse_args

def format(filename):
    """
    Formats for verbose output
    """
    msg = filename + ' has been un-signed.'
    return msg

def gen_summary(count):
    """
    Generates the stats
    """
    stats = ''
    stats += '\nTotal un-signed Files: ' + str(count)
    return stats

if __name__ == '__main__':
    args = parse_args()

    target= args.target
    if not os.path.exists(target):
        raise IOError('file/dir \'%s\' does not exist.' %(target))

    count = 0
    for filename in main.removeSignFiles(target, args.recursive):
        count += 1
        if args.verbose:
            print format(filename)

    if args.verbose:
        print gen_summary(count)

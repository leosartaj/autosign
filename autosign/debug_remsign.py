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
import sys
import main
import config
from parse.remsign_options import parse_args

def format_signrc(signrc):
    """
    formatting for signrc
    """
    msg =  'using ' + signrc + ' as rc'
    return msg

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

    if args.init:
        signrc = config.save_rc(config.gen_basic_rc())
    if args.signrc:
        signrc = args.signrc
        if not os.path.isfile(signrc):
            raise IOError('file \'%s\' does not exist.' %(signrc))
    else:
        signrc = config.find_rc()
    if not signrc: # hack for now
        print 'No Signrc found. Exiting.'
        sys.exit()

    sections = config.parse_rc(signrc)

    target= args.target
    if not os.path.exists(target):
        raise IOError('file/dir \'%s\' does not exist.' %(target))

    if args.verbose:
        print format_signrc(signrc), '\n'

    count = 0
    for section in sections:
        options = sections[section]
        for filename in main.removeSignFiles(target, options, args.recursive):
            count += 1
            if args.verbose:
                print format(filename)

    if args.verbose:
        print gen_summary(count)

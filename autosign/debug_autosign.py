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

if __name__ == '__main__':
    args = parse_args()

    signfile = args.signfile
    if not os.path.isfile(signfile):
        raise IOError('file \'%s\' does not exist.' %(signfile))
    target= args.target
    if not os.path.exists(target):
        raise IOError('file/dir \'%s\' does not exist.' %(target))
    main.signFiles(signfile, target, args.recursive, args.force)

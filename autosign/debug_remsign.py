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

if __name__ == '__main__':
    args = parse_args()

    target= args.target
    if not os.path.exists(target):
        raise IOError('file/dir \'%s\' does not exist.' %(target))
    main.removeSignFiles(target, args.recursive)

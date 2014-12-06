"""
For debugging purposes
"""

import os
import main
from options import parse_args

if __name__ == '__main__':
    options, args = parse_args()
    if args[0] == 'sign':
        signfile = args[1]
        if not os.path.isfile(signfile):
            raise IOError('file \'%s\' does not exist.' %(signfile))
        target = args[2]
        if not os.path.exists(target):
            raise IOError('file/dir \'%s\' does not exist.' %(target))
        main.signFiles(signfile, target, options.recursive, options.force)
    elif args[0] == 'rsign':
        target = args[1]
        if not os.path.exists(target):
            raise IOError('file/dir \'%s\' does not exist.' %(target))
        main.removeSignFiles(target, options.recursive)

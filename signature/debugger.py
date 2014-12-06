"""
For debugging purposes
"""

import os
import main
from options import parse_args

if __name__ == '__main__':
    options, args = parse_args()
    signfile = args[0]
    fName = args[1]
    main.signFiles(signfile, fName, options.recursive, options.force)

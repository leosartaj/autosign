#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

import shutil, os
from autosign import config

"""
Helper functions for performing tests
"""

def newFile(fName):
    """
    Touch a new file
    """
    with open(fName, 'a'):
        pass

def testArea(obj):
    obj.testArea = os.path.join(obj.dire, 'testArea')
    os.mkdir(obj.testArea)
    obj.unsigned1 = os.path.join(obj.dire, 'testArea/test_unsignedfile1.py')
    newFile(obj.unsigned1)
    obj.signed1 = os.path.join(obj.dire, 'testArea/test_signedfile1.py')
    shutil.copy(obj.signfile, obj.signed1)
    obj.testArea2 = os.path.join(obj.dire, 'testArea/testArea2')
    os.mkdir(obj.testArea2)
    obj.unsigned2 = os.path.join(obj.dire, 'testArea/testArea2/test_unsignedfile2.py')
    newFile(obj.unsigned2)
    obj.signed2 = os.path.join(obj.dire, 'testArea/testArea2/test_signedfile2.py')
    shutil.copy(obj.signfile, obj.signed2)

def readrc(obj):
    obj.signrc = os.path.join(obj.dire, 'testData/signrc')
    parser = config.gen_parser(obj.signrc)
    obj.options_py  = config.parse_section(parser, 'python')
    obj.options_c  = config.parse_section(parser, 'c')

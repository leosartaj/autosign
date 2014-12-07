#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

import unittest
import os
from autosign.main import getIndex

class TestgetIndex(unittest.TestCase):
    """
    tests the getIndex function in main module
    """
    def test_signed_files(self):
        dire = os.path.dirname(__file__)
        path = os.path.join(dire, 'testData/signed')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            start, end = getIndex(fName)
            self.assertNotEqual(start, None)
            self.assertNotEqual(end, None)
            length = end - start
            self.assertNotEqual(length, 0)

    def test_unsigned_files(self):
        dire = os.path.dirname(__file__)
        path = os.path.join(dire, 'testData/unsigned')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            start, end = getIndex(fName)
            self.assertEqual(start, None)
            self.assertEqual(end, None)

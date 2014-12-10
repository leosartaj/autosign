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
import helper
from autosign.main import getIndex

class TestgetIndex(unittest.TestCase):
    """
    tests the getIndex function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        helper.readrc(self)

    def test_signed_files_py(self):
        path = os.path.join(self.dire, 'testData/signed/py')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            start, end = getIndex(fName, self.options_py)
            self.assertNotEqual(start, None)
            self.assertNotEqual(end, None)
            length = end - start
            self.assertNotEqual(length, 0)

    def test_signed_files_c(self):
        path = os.path.join(self.dire, 'testData/signed/c')
        print self.options_c
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            print fName
            start, end = getIndex(fName, self.options_c)
            self.assertNotEqual(start, None)
            self.assertNotEqual(end, None)
            length = end - start
            self.assertNotEqual(length, 0)

    def test_unsigned_files(self):
        dire = os.path.dirname(__file__)
        path = os.path.join(dire, 'testData/unsigned')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            start, end = getIndex(fName, self.options_py)
            self.assertEqual(start, None)
            self.assertEqual(end, None)

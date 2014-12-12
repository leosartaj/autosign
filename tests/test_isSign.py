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
from autosign.main import isSign

class TestisSign(unittest.TestCase):
    """
    tests the isSign function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        helper.readrc(self)

    def test_signed_files_py(self):
        path = os.path.join(self.dire, 'testData/signed/py')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            self.assertEqual(isSign(fName, self.options_py), True)

    def test_signed_files_c(self):
        path = os.path.join(self.dire, 'testData/signed/c')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            self.assertEqual(isSign(fName, self.options_c), True)

    def test_unsigned_files(self):
        path = os.path.join(self.dire, 'testData/unsigned')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            self.assertEqual(isSign(fName, self.options_py), False)

#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

import unittest
import os, shutil
import helper
from autosign.main import checkFiles, isSign

class TestcheckTemplate(unittest.TestCase):
    """
    tests the checkFiles function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.signfile = os.path.join(self.dire, 'testData/dummySign.py')
        helper.testArea(self)

    def test_checkFiles_not_recursive(self):
        count = 0
        for filename, val in checkFiles(self.testArea):
            count += 1
            self.assertEqual(isSign(filename), val)
        self.assertEqual(count, 2)

    def test_checkFiles_recursive(self):
        count = 0
        for filename, val in checkFiles(self.testArea, True):
            count += 1
            self.assertEqual(isSign(filename), val)
        self.assertEqual(count, 4)

    def tearDown(self):
        shutil.rmtree(self.testArea)

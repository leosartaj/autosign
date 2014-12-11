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
from autosign.main import signFiles, isSign

class TestsignFiles(unittest.TestCase):
    """
    tests the signFiles function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.signfile = os.path.join(self.dire, 'testData/dummySign.py')
        self.unsigned = os.path.join(self.dire, 'testData/test_unsignedfile.py')
        helper.newFile(self.unsigned)
        helper.testArea(self)
        helper.readrc(self)

    def test_signFiles_on_file(self):
        self.assertFalse(isSign(self.unsigned, self.options_py))
        for filename, val in signFiles(self.signfile, self.unsigned, self.options_py):
            self.assertTrue(val)

    def test_signFiles_on_dir_not_recursive(self):
        count = 0
        for filename, val in signFiles(self.signfile, self.testArea, self.options_py):
            if val:
                count += 1
        self.assertEqual(count, 1)

    def test_signFiles_on_dir_not_recursive_forced(self):
        count = 0
        for filename, val in signFiles(self.signfile, self.testArea, self.options_py, False, True):
            if val:
                count += 1
        self.assertEqual(count, 2)

    def test_signFiles_on_dir_recursive(self):
        count = 0
        for filename, val in signFiles(self.signfile, self.testArea, self.options_py, True):
            if val:
                count += 1
        self.assertEqual(count, 2)

    def test_signFiles_on_dir_recursive_forced(self):
        count = 0
        for filename, val in signFiles(self.signfile, self.testArea, self.options_py, True, True):
            if val:
                count += 1
        self.assertEqual(count, 4)

    def tearDown(self):
        os.remove(self.unsigned)
        shutil.rmtree(self.testArea)

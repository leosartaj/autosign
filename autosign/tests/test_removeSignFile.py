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
from autosign.main import removeSignFiles, isSign

class TestsignFiles(unittest.TestCase):
    """
    tests the signFiles function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.signfile = os.path.join(self.dire, 'testData/dummySign.py')
        helper.testArea(self)

    def test_removeSignFiles_on_signed_file(self):
        self.assertTrue(isSign(self.signed1))
        removeSignFiles(self.signed1)
        self.assertFalse(isSign(self.signed1))

    def test_removeSignFiles_on_unsigned_file(self):
        self.assertFalse(isSign(self.unsigned1))
        removeSignFiles(self.unsigned1)
        self.assertFalse(isSign(self.unsigned1))

    def test_removeSignFiles_on_dir_not_recursive(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        removeSignFiles(self.testArea)
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertFalse(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def test_signFiles_on_dir_recursive(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        removeSignFiles(self.testArea, True)
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertFalse(isSign(self.signed1))
        self.assertFalse(isSign(self.signed2))

    def tearDown(self):
        shutil.rmtree(self.testArea)


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

    def test_signFiles_on_file(self):
        self.assertFalse(isSign(self.unsigned))
        self.assertTrue(isSign(self.signed1))
        signFiles(self.signfile, self.unsigned)
        self.assertTrue(isSign(self.unsigned))
        self.assertTrue(isSign(self.signed1))

    def test_signFiles_on_dir_not_recursive(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        signFiles(self.signfile, self.testArea)
        self.assertTrue(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def test_signFiles_on_dir_not_recursive_forced(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        signFiles(self.signfile, self.testArea, False, True)
        self.assertTrue(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def test_signFiles_on_dir_recursive(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        signFiles(self.signfile, self.testArea, True)
        self.assertTrue(isSign(self.unsigned1))
        self.assertTrue(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def test_signFiles_on_dir_recursive_forced(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        signFiles(self.signfile, self.testArea, True, True)
        self.assertTrue(isSign(self.unsigned1))
        self.assertTrue(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def tearDown(self):
        os.remove(self.unsigned)
        shutil.rmtree(self.testArea)

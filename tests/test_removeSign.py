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
from autosign.main import removeSign, isSign
from autosign.exce import UnsignedError

class TestremoveSign(unittest.TestCase):
    """
    tests the removeSign function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.signedfile = os.path.join(self.dire, 'testData/toBeSigned.py')
        self.signed = os.path.join(self.dire, 'testData/test_signedfile.py')
        shutil.copyfile(self.signedfile, self.signed)
        self.unsigned = os.path.join(self.dire, 'testData/test_unsignedfile.py')
        helper.newFile(self.unsigned)
        helper.readrc(self)

    def test_remove_from_unsigned_file(self):
        self.assertRaises(UnsignedError, removeSign, self.unsigned, self.options_py)

    def test_remove_from_signed_file(self):
        self.assertTrue(isSign(self.signed, self.options_py))
        removeSign(self.signed, self.options_py)
        self.assertFalse(isSign(self.signed, self.options_py))

    def tearDown(self):
        os.remove(self.unsigned)


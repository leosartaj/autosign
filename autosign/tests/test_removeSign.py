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
from autosign.exceptions import UnsignedError

class TestremoveSign(unittest.TestCase):
    """
    tests the removeSign function in main module
    """
    def setUp(self):
        dire = os.path.dirname(__file__)
        self.signedfile = os.path.join(dire, 'testData/toBeSigned.py')
        self.signed = os.path.join(dire, 'testData/test_signedfile.py')
        shutil.copyfile(self.signedfile, self.signed)
        self.unsigned = os.path.join(dire, 'testData/test_unsignedfile.py')
        helper.newFile(self.unsigned)

    def test_remove_from_unsigned_file(self):
        self.assertRaises(UnsignedError, removeSign, self.unsigned)

    def test_remove_from_signed_file(self):
        self.assertTrue(isSign(self.signed))
        removeSign(self.signed)
        self.assertFalse(isSign(self.signed))

    def tearDown(self):
        os.remove(self.unsigned)


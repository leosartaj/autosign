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
from autosign.main import sign, isSign
from autosign.exceptions import TemplateError

class Testsign(unittest.TestCase):
    """
    tests the getIndex function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.signfile = os.path.join(self.dire, 'testData/dummySign.py')
        self.otherSignfile = os.path.join(self.dire, 'testData/otherSign.py')
        self.shortSign = os.path.join(self.dire, 'testData/shortSign.py')
        self.longSign = os.path.join(self.dire, 'testData/longSign.py')

        self.toBeSigned = os.path.join(self.dire, 'testData/toBeSigned.py')
        self.signed = os.path.join(self.dire, 'testData/test_signedfile.py')
        shutil.copyfile(self.toBeSigned, self.signed)

        self.unsigned = os.path.join(self.dire, 'testData/test_unsignedfile.py')
        helper.newFile(self.unsigned)

    def test_incorrect_signfile(self):
        incorrect = os.path.join(self.dire, 'testData/unsigned')
        for filename in os.listdir(incorrect):
            path = os.path.join(incorrect, filename)
            self.assertRaises(TemplateError, sign, path, self.unsigned)

    def test_sign_on_unsigned_files(self):
        unsigned = self.unsigned
        self.assertEqual(isSign(unsigned), False)
        sign(self.signfile, unsigned)
        self.assertEqual(isSign(unsigned), True)
        os.remove(unsigned)

    def test_sign_on_signed_files_sign_same_length(self):
        signed = self.signed
        self.assertEqual(isSign(signed), True)
        sign(self.otherSignfile, signed, True)
        self.assertEqual(isSign(signed), True)

    def test_sign_on_signed_files_sign_shorter_length(self):
        signed = self.signed
        self.assertEqual(isSign(signed), True)
        sign(self.shortSign, signed, True)
        self.assertEqual(isSign(signed), True)

    def test_sign_on_signed_files_sign_longer_length(self):
        signed = self.signed
        self.assertEqual(isSign(signed), True)
        sign(self.longSign, signed, True)
        self.assertEqual(isSign(signed), True)

    def tearDown(self):
        os.remove(self.signed)

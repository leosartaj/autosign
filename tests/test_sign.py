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
from autosign.exce import TemplateError

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
        helper.readrc(self)

    def test_incorrect_signfile(self):
        incorrect = os.path.join(self.dire, 'testData/unsigned')
        for filename in os.listdir(incorrect):
            path = os.path.join(incorrect, filename)
            self.assertRaises(TemplateError, sign, path, self.unsigned, self.options_py)

    def test_sign_on_unsigned_files(self):
        unsigned = self.unsigned
        self.assertEqual(isSign(unsigned, self.options_py), False)
        sign(self.signfile, unsigned, self.options_py)
        self.assertEqual(isSign(unsigned, self.options_py), True)
        os.remove(unsigned)

    def test_sign_on_signed_files_ext_c(self):
        cdir = os.path.join(self.dire, 'testData/signed/c')
        cfile = os.path.join(self.dire, 'testData/signed/c/test1.c')
        template = os.path.join(self.dire, 'test1.c')
        path = os.path.join(self.dire, 'c')
        shutil.copytree(cdir, path)
        shutil.copy(cfile, template)
        for filename in os.listdir(path):
            fName  = os.path.join(path, filename)
            self.assertEqual(isSign(fName, self.options_c), True)
            sign(template, fName, self.options_c, True)
            self.assertEqual(isSign(fName, self.options_c), True)
        shutil.rmtree(path)
        os.remove(template)

    def test_sign_on_signed_files_sign_same_length(self):
        signed = self.signed
        self.assertEqual(isSign(signed, self.options_py), True)
        sign(self.otherSignfile, signed, self.options_py, True)
        self.assertEqual(isSign(signed, self.options_py), True)

    def test_sign_on_signed_files_sign_shorter_length(self):
        signed = self.signed
        self.assertEqual(isSign(signed, self.options_py), True)
        sign(self.shortSign, signed, self.options_py, True)
        self.assertEqual(isSign(signed, self.options_py), True)

    def test_sign_on_signed_files_sign_longer_length(self):
        signed = self.signed
        self.assertEqual(isSign(signed, self.options_py), True)
        sign(self.longSign, signed, self.options_py, True)
        self.assertEqual(isSign(signed, self.options_py), True)

    def tearDown(self):
        os.remove(self.signed)

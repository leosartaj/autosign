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
from autosign.main import checkTemplate

class TestcheckTemplate(unittest.TestCase):
    """
    tests the checkTemplate function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        helper.readrc(self)

    def test_correct_template_py(self):
        path = os.path.join(self.dire, 'testData/signed/py')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            result = checkTemplate(fName, self.options_py)
            self.assertEqual(result, True)

    def test_correct_template_c(self):
        path = os.path.join(self.dire, 'testData/signed/c')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            result = checkTemplate(fName, self.options_c)
            self.assertEqual(result, True)

    def test_incorrect_template(self):
        path = os.path.join(self.dire, 'testData/unsigned')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            self.assertEqual(checkTemplate(fName, self.options_py), False)

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
from autosign.main import checkTemplate

class TestcheckTemplate(unittest.TestCase):
    """
    tests the checkTemplate function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_correct_template(self):
        signfile = os.path.join(self.dire, 'testData/dummySign.py')
        self.assertEqual(checkTemplate(signfile), True)

    def test_incorrect_template(self):
        path = os.path.join(self.dire, 'testData/unsigned')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            self.assertEqual(checkTemplate(fName), False)

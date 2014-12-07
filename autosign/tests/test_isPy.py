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
from autosign.main import isPy

class TestcheckTemplate(unittest.TestCase):
    """
    tests the isPy function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_isPy_not_python_file(self):
        simplefile = os.path.join(self.dire, 'test_simplefile')
        helper.newFile(simplefile)
        self.assertFalse(isPy(simplefile))
        os.remove(simplefile)

    def test_isPy_python_file(self):
        pythonfile = os.path.join(self.dire, 'test_pythonfile.py')
        helper.newFile(pythonfile)
        self.assertTrue(isPy(pythonfile))
        os.remove(pythonfile)

    def test_isPy_python_file_no_ext(self):
        pythonfile = os.path.join(self.dire, 'test_pythonfile')
        stored = os.path.join(self.dire, 'testData/pythonfile')
        shutil.copyfile(stored, pythonfile)
        self.assertTrue(isPy(pythonfile))
        os.remove(pythonfile)

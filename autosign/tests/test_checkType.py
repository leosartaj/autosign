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
from autosign.main import checkType

class TestcheckTemplate(unittest.TestCase):
    """
    tests the checkType function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        helper.readrc(self)

    def test_checkType_not_python_file(self):
        simplefile = os.path.join(self.dire, 'test_simplefile')
        helper.newFile(simplefile)
        ext, re = self.options_py.ext, self.options_py.allow
        self.assertFalse(checkType(simplefile, ext, re))
        os.remove(simplefile)

    def test_checkType_python_file(self):
        pythonfile = os.path.join(self.dire, 'test_pythonfile.py')
        helper.newFile(pythonfile)
        ext, re = self.options_py.ext, self.options_py.allow
        self.assertTrue(checkType(pythonfile, ext, re))
        os.remove(pythonfile)

    def test_checkType_python_file_no_ext(self):
        pythonfile = os.path.join(self.dire, 'test_pythonfile')
        stored = os.path.join(self.dire, 'testData/pythonfile')
        shutil.copyfile(stored, pythonfile)
        ext, re = self.options_py.ext, self.options_py.allow
        self.assertTrue(checkType(pythonfile, ext, re))
        os.remove(pythonfile)

    def test_checkType_c_file(self):
        path = os.path.join(self.dire, 'testData/signed/c')
        ext, re = self.options_c.ext, None
        for filename in os.listdir(path):
            self.assertTrue(checkType(filename, ext, re))

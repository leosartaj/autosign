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
from autosign.main import removeInter, checkType

class TestcheckTemplate(unittest.TestCase):
    """
    tests the removeInter function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        helper.readrc(self)

    def test_removeInter_not_hasInter(self):
        simplefile = os.path.join(self.dire, 'test_simplefile')
        helper.newFile(simplefile)
        self.assertEqual(removeInter(simplefile, self.options_py.allow), None)
        os.remove(simplefile)

    def test_removeInter_hasInter(self):
        pythonfile = os.path.join(self.dire, 'test_pythonfile.py')
        stored = os.path.join(self.dire, 'testData/pythonfile')
        shutil.copyfile(stored, pythonfile)
        ext = self.options_py.ext
        self.assertTrue(checkType(pythonfile, ext))
        self.assertNotEqual(removeInter(pythonfile, self.options_py.allow), None)
        os.remove(pythonfile)


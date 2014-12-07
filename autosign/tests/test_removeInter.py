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
from autosign.main import removeInter, isPy

class TestcheckTemplate(unittest.TestCase):
    """
    tests the removeInter function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_removeInter_not_hasInter(self):
        simplefile = os.path.join(self.dire, 'test_simplefile')
        helper.newFile(simplefile)
        self.assertEqual(removeInter(simplefile), None)
        os.remove(simplefile)

    def test_removeInter_hasInter(self):
        pythonfile = os.path.join(self.dire, 'test_pythonfile')
        stored = os.path.join(self.dire, 'testData/pythonfile')
        shutil.copyfile(stored, pythonfile)
        self.assertTrue(isPy(pythonfile))
        removeInter(pythonfile)
        self.assertFalse(isPy(pythonfile))
        os.remove(pythonfile)


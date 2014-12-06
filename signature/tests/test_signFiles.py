import unittest
import os, shutil
from signature.main import signFiles, isSign

class TestsignFiles(unittest.TestCase):
    """
    tests the signFiles function in main module
    """
    def _newFile(self, fName):
        with open(fName, 'a'):
            pass

    def _testArea(self):
        self.testArea = os.path.join(self.dire, 'testArea')
        os.mkdir(self.testArea)
        self.unsigned1 = os.path.join(self.dire, 'testArea/test_unsignedfile1.py')
        self._newFile(self.unsigned1)
        self.signed1 = os.path.join(self.dire, 'testArea/test_signedfile1.py')
        shutil.copy(self.signfile, self.signed1)
        self.testArea2 = os.path.join(self.dire, 'testArea/testArea2')
        os.mkdir(self.testArea2)
        self.unsigned2 = os.path.join(self.dire, 'testArea/testArea2/test_unsignedfile2.py')
        self._newFile(self.unsigned2)
        self.signed2 = os.path.join(self.dire, 'testArea/testArea2/test_signedfile2.py')
        shutil.copy(self.signfile, self.signed2)

    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.signfile = os.path.join(self.dire, 'testData/dummySign.py')
        self.unsigned = os.path.join(self.dire, 'testData/test_unsignedfile.py')
        self._newFile(self.unsigned)
        self._testArea()

    def test_signFiles_on_file(self):
        self.assertFalse(isSign(self.unsigned))
        self.assertTrue(isSign(self.signed1))
        signFiles(self.signfile, self.unsigned)
        self.assertTrue(isSign(self.unsigned))
        self.assertTrue(isSign(self.signed1))

    def test_signFiles_on_dir_not_recursive(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        signFiles(self.signfile, self.testArea)
        self.assertTrue(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def test_signFiles_on_dir_not_recursive_forced(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        signFiles(self.signfile, self.testArea, False, True)
        self.assertTrue(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def test_signFiles_on_dir_recursive(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        signFiles(self.signfile, self.testArea, True)
        self.assertTrue(isSign(self.unsigned1))
        self.assertTrue(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def test_signFiles_on_dir_recursive_forced(self):
        self.assertFalse(isSign(self.unsigned1))
        self.assertFalse(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))
        signFiles(self.signfile, self.testArea, True, True)
        self.assertTrue(isSign(self.unsigned1))
        self.assertTrue(isSign(self.unsigned2))
        self.assertTrue(isSign(self.signed1))
        self.assertTrue(isSign(self.signed2))

    def tearDown(self):
        os.remove(self.unsigned)
        shutil.rmtree(self.testArea)

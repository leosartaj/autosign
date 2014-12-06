import unittest
import os, shutil
from signature.main import sign, isSign
from signature.exceptions import TemplateError

class Testsign(unittest.TestCase):
    """
    tests the getIndex function in main module
    """
    def setUp(self):
        dire = os.path.dirname(__file__)

        self.signfile = os.path.join(dire, 'testData/dummySign.py')
        self.signed = os.path.join(dire, 'testData/test_signedfile.py')
        self.incorrect = os.path.join(dire, 'testData/unsigned')
        shutil.copyfile(self.signfile, self.signed)
        self.unsigned = os.path.join(dire, 'testData/test_unsignedfile.py')
        with open(self.unsigned, 'w'):
            pass

    def test_incorrect_signfile(self):
        for filename in os.listdir(self.incorrect):
            path = os.path.join(self.incorrect, filename)
            self.assertRaises(TemplateError, sign, path, self.unsigned)

    def test_sign_on_unsigned_files(self):
        unsigned = self.unsigned
        self.assertEqual(isSign(unsigned), False)
        sign(self.signfile, unsigned)
        self.assertEqual(isSign(unsigned), True)

    def test_sign_on_signed_files(self):
        signed = self.signed
        self.assertEqual(isSign(signed), True)
        sign(self.signfile, signed)
        self.assertEqual(isSign(signed), True)

    def tearDown(self):
        os.remove(self.unsigned)
        os.remove(self.signed)

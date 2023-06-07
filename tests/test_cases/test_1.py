from unittest import TestCase
from decoder import runner

class test1(TestCase):

    def positive_test(self):

        result = runner.decoder_class
        self.assertTrue(result)
        self.assertEquals()

    def negative_test(self):
        self.assertFalse()


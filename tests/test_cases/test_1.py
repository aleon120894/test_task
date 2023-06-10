from unittest import TestCase
from decoder import runner

class test1(TestCase):

    def positive_test(self, check_data):

        result = runner.decoder_class
        self.assertTrue(result)
        self.assertEquals(check_data, result)

    def negative_test(self):
        self.assertFalse()


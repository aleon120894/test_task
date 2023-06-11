from unittest import TestCase
from decoder import runner

class test1(TestCase):

    def positive_test(self, test_data):

        result = runner.decoder_class
        self.assertTrue(result)
        self.assertEquals(test_data, result)

    def negative_test(self, test_data):

        result = runner.decoder_class
        self.assertTrue(result)
        self.assertNotEquals(result, test_data)

    def empty_test(self):

        result = runner.decoder_class
        test_data = {}
        self.assertNotEquals(result, test_data)


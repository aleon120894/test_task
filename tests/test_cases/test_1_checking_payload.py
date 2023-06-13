from unittest import TestCase

class test1(TestCase):

    def positive_test(self):

        self.assertTrue(True)

    def negative_test(self):
        self.assertTrue(False)

    def empty_test(self):
        result_data = ''
        self.assertIsNone(result_data)

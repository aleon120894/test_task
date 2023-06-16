from unittest import TestCase


class Test1(TestCase):

    def positive_test(self, test_data, payload):

        self.assertEquals(test_data, payload)

    def negative_test(self, test_data, payload):
        self.assertFalse(test_data == payload)

    def empty_test(self):
        result_data = ''
        self.assertIsNone(result_data)

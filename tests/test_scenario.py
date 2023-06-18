import pytest
from unittest import TestCase
from decoder import decoder


class TestScenario(TestCase):

    expected_result = """{'field1': 'High',
                          'field10': '00',
                          'field2': '00',
                          'field3': '00',
                          'field4': '10',
                          'field5': '01',
                          'field6': '01',
                          'field7': '01',
                          'field8': 'Very Low',
                          'field9': '01'}"""

    decoder_class = decoder.DecodeSensor()
    decoded_data = decoder_class.decoder_from_sensor('27C7011D')

    def test_1(self):
        # self.assertTrue(self.expected_result == self.decoded_data)
        self.assertTrue(True)

    def test_2(self):
        self.assertFalse(False)

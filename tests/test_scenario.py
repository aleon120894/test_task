import pytest
from unittest import TestCase
from decoder import decoder
from .test_config import test_data


class TestScenario(TestCase):

    # Main scenario for executing tests with positive result (valid data), and different negative results (invalid fields)

    decoder_class = decoder.DecodeSensor()
    decoded_data = decoder_class.decoder_from_sensor('27C7011D')
    data_for_tests = test_data.TestData()

    @pytest.fixture(name="Test with valid data")
    def test_for_all_fields_valid(self):
        valid_data = self.data_for_tests.get_valid_data()
        self.assertEqual(self.decoded_data, valid_data)

    @pytest.fixture(name="Test with invalid field 1")
    def test_for_invalid_field_1(self):
        invalid_field_1 = self.data_for_tests.get_data_with_invalid_field_1()
        self.assertEqual(self.decoded_data, invalid_field_1)

    @pytest.fixture(name="Test with invalid field 2")
    def test_for_invalid_field_2(self):
        invalid_field_2 = self.data_for_tests.get_data_with_invalid_field_2()
        self.assertEqual(self.decoded_data, invalid_field_2)

    @pytest.fixture(name="Test with invalid field 3")
    def test_for_invalid_field_3(self):
        invalid_field_3 = self.data_for_tests.get_data_with_invalid_field_3()
        self.assertEqual(self.decoded_data, invalid_field_3)

    @pytest.fixture(name="Test with invalid field 4")
    def test_for_invalid_field_4(self):
        invalid_field_4 = self.data_for_tests.get_data_with_invalid_field_4()
        self.assertEqual(self.decoded_data, invalid_field_4)

    @pytest.fixture(name="Terst with invalid all fields")
    def test_for_invalid_all_fields(self):
        invalid_data = self.data_for_tests.get_invalid_empty_data()
        self.assertEqual(self.decoded_data, invalid_data)


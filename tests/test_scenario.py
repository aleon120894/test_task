import pytest
from unittest import TestCase
from decoder import decoder


class TestScenario(TestCase):

    valid_data = """
    [
    {
        "field1": 199
    },
    {
        "field4": 1
    },
    {
        "field8": 29
    }
]
"""
    data_with_invalid_field_1 = """[
    {
        "field1": 
    },
    {
        "field4": 1
    },
    {
        "field8": 29
    }
]
"""

    data_with_invalid_field_4 = """[
    {
        "field1": 199
    },
    {
        "field4": 
    },
    {
        "field8": 29
    }
]
"""

    data_with_invalid_field_8 =  """
    [
    {
        "field1": 199
    },
    {
        "field4": 1
    },
    {
        "field8": 
    }
]
"""

    data_with_invalid_all_fields =  """
    [
    {
        "field1": 
    },
    {
        "field4": 
    },
    {
        "field8": 
    }
]
"""

    decoder_class = decoder.DecodeSensor()
    decoded_data = decoder_class.decoder_from_sensor('27C7011D')

    @pytest.mark.parametrize("decoded_data", valid_data)
    def test_for_all_fields_valid(self):
        self.assertEqual(self.decoded_data, self.valid_data)

    @pytest.mark.parametrize("decoded_data", data_with_invalid_field_1)
    def test_for_invalid_field_1(self):
        self.assertEqual(self.decoded_data, self.data_with_invalid_field_1)

    @pytest.mark.parametrize("decoded_data", data_with_invalid_field_4)
    def test_for_invalid_field_4(self):
        self.assertEqual(self.decoded_data, self.data_with_invalid_field_4)

    @pytest.mark.parametrize("decoded_data", data_with_invalid_field_8)
    def test_for_invalid_field_8(self):
        self.assertEqual(self.decoded_data, self.data_with_invalid_field_8)

    @pytest.mark.parametrize("decoded_data", data_with_invalid_all_fields)
    def test_for_invalid_all_fields(self):
        self.assertEqual(self.decoded_data, self.data_with_invalid_all_fields)


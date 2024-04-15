import pytest
from decoder import decode_payload


@pytest.mark.parametrize("payload, expected_result", [
    ("27C7011D", {'field1': 'High', 'field10': '00', 'field2': '00', 'field3': '00', 'field4': '10',
                  'field5': '01', 'field6': '01', 'field7': '01', 'field8': 'Very Low', 'field9': '01'}),
    # Add more test cases here if needed
])


def test_decode_payload(payload, expected_result):

    payload_string, expected_result = payload
    result = decode_payload(payload_string)

    print("Expected:", expected_result)
    print("Actual:", result)
    assert result == expected_result


if __name__ == "__main":
    pytest.main()

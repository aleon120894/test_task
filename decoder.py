def decode_payload(payload):

    # Field values dictionaries
    field1 = {'000': 'Low', '111': 'High'}
    field4 = {'000': '00', '001': '10', '010': '20', '011': '30', '100': '40', '101': '50', '110': '60', '111': '70'}
    field8 = {'000': 'Very Low', '001': 'Low', '010': 'Medium', '011': 'High', '100': 'reserved', '101': 'reserved', '110': 'reserved', '111': 'reserved'}

    # Initialize result dictionary
    result = {}

    # Format settings - array [sett_byte1 as dict {bit: [size, 'field_name']}, sett_byte2, sett_byte3, sett_byte4]
    device_settings = [
        {0: [3, 'field1'], 3: [1, 'field2'], 4: [1, 'field3'], 5: [3, 'field4']},
        {0: [1, 'field5'], 1: [1, 'field6'], 2: [1, 'field7'], 3: [3, 'field8']},
        {0: [1, 'field9'], 5: [1, 'field10']}
    ]

    # Convert payload to binary
    binary_payload = bin(int(payload, 16))[2:].zfill(len(payload) * 4)

    # Loop through device settings to decode parameters
    for byte_idx, byte_settings in enumerate(device_settings):
        for bit, (size, field_name) in byte_settings.items():

            # Get bits corresponding to the parameter
            start_bit = byte_idx * 8 + bit
            end_bit = start_bit + size
            param_bits = binary_payload[start_bit:end_bit]

            # Decode parameter value using corresponding dictionary
            param_value = field1.get(param_bits, 'reserved') if field_name == 'field1' else \
                          field4.get(param_bits, 'reserved') if field_name == 'field4' else \
                          field8.get(param_bits, 'reserved')

            # Add parameter to result dictionary
            result[field_name] = param_value

    return result

payload = ("27C7011D", {'field1': 'High', 'field10': '00', 'field2': '00', 'field3': '00', 'field4': '10',
                      'field5': '01', 'field6': '01', 'field7': '01', 'field8': 'Very Low', 'field9': '01'})

payload_string, expected_result = payload

def test_decode_payload(payload, expected_result):

    print("Payload: ", payload)
    payload_string, expected_result = payload
    print("Payload string: ", payload_string)

    print("Expected result: ", expected_result)
    result = decode_payload(payload_string)

    print("Expected:", expected_result)
    print("Actual:", result)
    assert result == expected_result

if __name__ == "__main__":
    test_decode_payload(payload_string, expected_result)




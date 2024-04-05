def decode_payload(payload):
    # Field values dictionaries
    field1 = {'0': 'Low', '7': 'High'}
    field4 = {'0': '00', '1': '10', '2': '20', '3': '30', '4': '40', '5': '50', '6': '60', '7': '70'}
    field8 = {'0': 'Very Low', '2': 'Low', '4': 'Medium', '5': 'High', '7': 'Very High'}

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

            # Convert binary to decimal
            param_value = str(int(param_bits, 2))

            # Decode parameter value using corresponding dictionary
            if field_name == 'field1':
                param_value = field1.get(param_value, 'reserved')
            elif field_name == 'field4':
                param_value = field4.get(param_value, 'reserved')
            elif field_name == 'field8':
                param_value = field8.get(param_value, 'reserved')

            # Add parameter to result dictionary
            result[field_name] = param_value

    return result
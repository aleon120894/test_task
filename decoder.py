def decode_payload(payload):
    # Field values dictionaries
    field1 = {'000': 'Low', '111': 'High'}
    field4 = {'000': '00', '001': '10', '010': '20', '011': '30', '100': '40', '101': '50', '110': '60', '111': '70'}
    field8 = {'000': 'Very Low', '001': 'reserved', '010': 'Low', '011': 'reserved', '100': 'Medium', '101': 'High', '110': 'reserved', '111': 'Very High'}

    # Initialize result dictionary
    result = {}

    # Define device settings
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

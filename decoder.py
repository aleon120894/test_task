def decode_payload(payload):
    # Field values dictionaries
    field1 = {'000': 'Low', '111': 'High'}
    field4 = {'000': '00', '001': '10', '010': '20', '011': '30', '100': '40', '101': '50', '110': '60', '111': '70'}
    field8 = {'000': 'Very Low', '001': 'Low', '010': 'Medium', '011': 'High', '100': 'reserved', '101': 'reserved', '110': 'reserved', '111': 'reserved'}

    # Initialize result dictionary
    result = {}

    # Convert payload to binary
    binary_payload = bin(int(payload, 16))[2:].zfill(len(payload) * 4)

    # Loop through device settings to decode parameters
    for byte_idx, byte_settings in enumerate(device_settings):
        for bit, (size, field_name) in byte_settings.items():

            # Get bits corresponding to the parameter
            start_bit = byte_idx * 8 + bit
            end_bit = start_bit + size
            param_bits = binary_payload[start_bit:end_bit]

            # Debugging print statements
            print(f"Parameter Bits for {field_name}: {param_bits}")

            # Decode parameter value using corresponding dictionary
            param_value = field1.get(param_bits, 'reserved') if field_name == 'field1' else \
                          field4.get(param_bits, 'reserved') if field_name == 'field4' else \
                          field8.get(param_bits, 'reserved')

            # Debugging print statement
            print(f"Decoded value for {field_name}: {param_value}")

            # Add parameter to result dictionary
            result[field_name] = param_value

    return result


from multiprocessing.dummy import list
import binascii
import json

class DecodeSensor:

    def decoder_from_sensor(self, payload):

        binascii_decode = binascii.unhexlify(payload)
        decoded_data = list(bytearray(binascii_decode))

        first_part = decoded_data[1]
        second_part = decoded_data[2]
        third_part = decoded_data[3]

        field_1 = {"field1": first_part}
        field_4 = {"field4": second_part}
        field_8 = {"field8": third_part}

        decoded_json = [
            field_1,
            field_4,
            field_8,
        ]

        decoded = json.dumps(decoded_json, sort_keys=True, indent=4)

        print(decoded)

    def decoder_testing(self, test_data):
        assert test_data == self.decoder_from_sensor('27C7011D')



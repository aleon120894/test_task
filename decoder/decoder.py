import binascii
import base64
import json

class decodeSensor:

    def decoder_from_sensor(self, payload):

        binascii_decode = binascii.unhexlify(payload)

        first_part = binascii_decode[:2]
        second_part = binascii_decode[2:3]
        third_part = binascii_decode[3:4]

        device_settings = []

        fild_1 = []
        field_4 = []
        field_8 = []

        decoded_json = {}

        print(first_part)
        print(second_part)
        print(third_part)



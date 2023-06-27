from multiprocessing.dummy import list
import binascii
import json

class DecodeSensor:

    def decoder_from_sensor(self, payload):

        binascii_decode = binascii.unhexlify(payload)
        decoded_data = list(bytearray(binascii_decode))

        for data in decoded_data:
            print(data)



import binascii
import base64

class decodeSensor:

    def decoder_from_sensor(self, payload):

        field_1 = []
        field_4 = []
        field_8 = []

        binascii_decode = binascii.unhexlify(payload)
        print(binascii_decode)



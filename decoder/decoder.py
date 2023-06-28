from multiprocessing.dummy import list
import binascii
import json

class DecodeSensor:

    def decoder_from_sensor(self, payload):

        binascii_decode = binascii.unhexlify(payload)
        decoded_data = list(bytearray(binascii_decode))
        data_for_json_encoding = {
            "field1": decoded_data[0],
            "field2": decoded_data[1],
            "field3": decoded_data[2],
            "field4": decoded_data[3]}

        encoded_json = json.dumps(data_for_json_encoding)
        return encoded_json


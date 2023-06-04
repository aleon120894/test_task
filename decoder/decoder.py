import json

class decodeJson:

    def decoder(self, json_for_decoding):

        decode_data = json.dump(json_for_decoding)
        field_1 = []
        field_4 = []
        field_8 = []


        for data in decode_data:
            if data[0:7] == "field1":
                field_1.add(data)

            elif data[0:7] == "field4":
                field_4.add(data)

            elif data[0:7] == "field8":
                field_8.add(data)

        return field_1, field_4, field_8

import json


class TestData:

    # Class for getting different test json for scenario
    def get_valid_data(self):
        valid_data = '{"field1": 39, "field2": 199, "field3": 1, "field4": 29}'
        valid_json = json.dumps(valid_data)
        return valid_json

    def get_data_with_invalid_field_1():
        data_with_invalid_field_1 = '{"field1": , "field2": 199, "field3": 1, "field4": 29}'
        data_with_invalid_field_1_json = json.dumps(data_with_invalid_field_1)
        return data_with_invalid_field_1_json

    def get_data_with_invalid_field_2():
        data_with_invalid_field_2 = '{"field1": 39: , "field2": , "field3": 1, "field4": 29}'
        data_with_invalid_field_2_json = json.dumps(data_with_invalid_field_2)
        return data_with_invalid_field_2_json

    def get_data_with_invalid_field_3():
        data_with_invalid_field_3 = '{"field1": 39: , "field2": 199, "field3": , "field4": 29}'
        data_with_invalid_field_3_json = json.dumps(data_with_invalid_field_3)
        return data_with_invalid_field_3_json

    def get_data_with_invalid_field_4():
        data_with_invalid_field_4 = '{"field1": 39: , "field2": 199, "field3": 1, "field4": }'
        data_with_invalid_field_4_json = json.dumps(data_with_invalid_field_4)
        return data_with_invalid_field_4_json

    def get_invalid_empty_data():
        invalid_data = '{ }'
        invalid_data_json = json.dumps(invalid_data)
        return invalid_data_json


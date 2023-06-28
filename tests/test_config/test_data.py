import json

class TestData:

    def get_valid_data(self):
        valid_data = '{"field1": 39, "field2": 199, "field3": 1, "field4": 29}'
        return valid_data

    def get_data_with_invalid_field_1():
        data_with_invalid_field_1 = '{"field1": , "field2": 199, "field3": 1, "field4": 29}'
        return data_with_invalid_field_1

    def get_data_with_invalid_field_2():
        data_with_invalid_field_2 = '{"field1": 39: , "field2": , "field3": 1, "field4": 29}'
        return data_with_invalid_field_2

    def get_data_with_invalid_field_3():
        data_with_invalid_field_3 = '{"field1": 39: , "field2": 199, "field3": , "field4": 29}'
        return data_with_invalid_field_3

    def get_data_with_invalid_field_4():
        data_with_invalid_field_4 = '{"field1": 39: , "field2": 199, "field3": 1, "field4": }'
        return data_with_invalid_field_4

    def get_invalid_data():

        invalid_data = '{ }'
        return invalid_data


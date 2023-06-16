import pytest


class TestScenario():

    def __init__(self):
        self.expected_result = """{'field1': 'High',
                                   'field10': '00',
                                   'field2': '00',
                                   'field3': '00',
                                   'field4': '10',
                                   'field5': '01',
                                   'field6': '01',
                                   'field7': '01',
                                   'field8': 'Very Low',
                                   'field9': '01'}"""

    @pytest.fixture(scope="session")
    def test_1(self):
        print("===================")
        print("Running first test")
        print("==================")

        self.test_1.positive_test(self.expected_result)

    def test_2(self):
        print("===================")
        print("Running second test")
        print("==================")

        self.test_1.negative_test(self.expected_result)

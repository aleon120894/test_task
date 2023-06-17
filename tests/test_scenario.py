import pytest
import test_cases.test_1_checking_payload


class TestScenario():

    expected_result = """{'field1': 'High',
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
    @pytest.mark.parametrize("expexted_result", expected_result)
    def test_1(self):

        print("===================")
        print("Running first test")
        print("==================")
        test_1_checking_payload.positive_test(self.expected_result)

    @pytest.mark.parametrize("expexted_result", " ")
    def test_2(self):

        print("===================")
        print("Running second test")
        print("==================")
        test_1.checking_payload.negative_test(self.expected_result)

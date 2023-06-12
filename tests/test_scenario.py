import pytest
import test_cases.test_1


class TestScenario():

    def __init__(self):
        pass

    @pytest.fixture
    def test_1(self):
        print("===================")
        print("Running first test")
        print("==================")

    def test_2(self):
        print("===================")
        print("Running second test")
        print("==================")

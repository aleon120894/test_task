
def pytest_addoption(parser):
    parser.ddoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc):

    if "decoded_data" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 2
        metafunc.parametrize("valid_data", range(end))


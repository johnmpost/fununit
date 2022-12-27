from fununit import UnitTest

class TestSuite:
    suite_name = None
    unit_tests = None

def create(suite_name, unit_tests):
    test_suite = TestSuite()
    test_suite.suite_name = suite_name
    test_suite.unit_tests = unit_tests
    return test_suite

def from_cases(suite_name, function_name, function, test_cases):
    test_suite = TestSuite()
    test_suite.suite_name = suite_name
    unit_tests = [UnitTest.from_case(function_name, function, test_case)
        for test_case in test_cases]
    test_suite.unit_tests = unit_tests
    return test_suite

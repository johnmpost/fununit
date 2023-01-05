class TestCase:
    parameters = None
    expected = None
    case_name = None

def create(parameters, expected, case_name = None):
    test_case = TestCase()
    test_case.parameters = parameters
    test_case.expected = expected
    test_case.case_name = case_name
    return test_case

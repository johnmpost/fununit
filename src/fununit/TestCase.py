class TestCase:
    parameters = None
    expected = None
    case_name = None

def create(case_name, parameters, expected):
    test_case = TestCase()
    test_case.case_name = case_name
    test_case.parameters = parameters
    test_case.expected = expected
    return test_case

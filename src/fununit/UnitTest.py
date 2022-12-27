class UnitTest:
    function_name = None
    function = None
    case_name = None
    parameters = None
    expected = None

def create(function_name, function, case_name, parameters, expected):
    unit_test = UnitTest()
    unit_test.function_name = function_name
    unit_test.function = function
    unit_test.case_name = case_name
    unit_test.parameters = parameters
    unit_test.expected = expected
    return unit_test

def from_case(function_name, function, test_case):
    unit_test = UnitTest()
    unit_test.function_name = function_name
    unit_test.function = function
    unit_test.case_name = test_case.case_name
    unit_test.parameters = test_case.parameters
    unit_test.expected = test_case.expected
    return unit_test

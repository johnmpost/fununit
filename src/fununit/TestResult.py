class TestResult:
    tags = None
    function_name = None
    case_name = None
    parameters = None
    expected = None
    actual = None
    passed = None

def create(tags, function_name, case_name, parameters, expected, actual, passed):
    test_result = TestResult()
    test_result.tags = tags
    test_result.function_name = function_name
    test_result.case_name = case_name
    test_result.parameters = parameters
    test_result.expected = expected
    test_result.actual = actual
    test_result.passed = passed
    return test_result

def get_actual_from_test(unit_test):
    params_is_dict = isinstance(unit_test.parameters, dict)
    actual = unit_test.function(**unit_test.parameters) \
        if params_is_dict \
        else unit_test.function(*unit_test.parameters)
    return actual

def from_test(unit_test):
    actual = get_actual_from_test(unit_test)
    return create(
        unit_test.tags,
        unit_test.function_name,
        unit_test.case_name,
        unit_test.parameters,
        unit_test.expected,
        actual,
        unit_test.equality_fn(unit_test.expected, actual)
    )

def from_tests(unit_tests):
    return [from_test(unit_test) for unit_test in unit_tests]

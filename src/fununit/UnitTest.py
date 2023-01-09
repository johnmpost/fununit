from functools import partial
from utils import structurally_equal

class UnitTest:
    equality_fn = None
    tags = None
    function_name = None
    function = None
    parameters = None
    expected = None
    case_name = None

def create(tags, function_name, function, parameters, expected, case_name = None):
    unit_test = UnitTest()
    unit_test.equality_fn = structurally_equal
    unit_test.tags = tags
    unit_test.function_name = function_name
    unit_test.function = function
    unit_test.parameters = parameters
    unit_test.expected = expected
    unit_test.case_name = case_name
    return unit_test

def from_case(tags, function_name, function, test_case):
    return create(
        tags,
        function_name,
        function,
        test_case.parameters,
        test_case.expected,
        test_case.case_name)

def create_many(tags, function_name, function, test_cases):
    return [from_case(tags, function_name, function, test_case)
        for test_case in test_cases]

def many_from_cases_with_tags(tags):
    return partial(create_many, tags)

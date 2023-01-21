from functools import partial
from fununit._utils import _structurally_equal
from fununit import TestCase

class UnitTest:
    equality_fn = None
    tags = None
    function_name = None
    function = None
    case_name = None
    parameters = None
    expected = None

def create(tags, function_name, function, case_name, parameters, expected):
    unit_test = UnitTest()
    unit_test.equality_fn = _structurally_equal
    unit_test.tags = tags
    unit_test.function_name = function_name
    unit_test.function = function
    unit_test.case_name = case_name
    unit_test.parameters = parameters
    unit_test.expected = expected
    return unit_test

def from_case(tags, function_name, function, test_case):
    return create(
        tags,
        function_name,
        function,
        test_case.case_name,
        test_case.parameters,
        test_case.expected)

def from_cases(tags, function_name, function, test_cases):
    return [from_case(tags, function_name, function, test_case)
        for test_case in test_cases]

def from_cases_implicit(tags, function_name, function, test_case_tuples):
    test_cases = [TestCase.create(*test_case_tuple)
        for test_case_tuple in test_case_tuples]
    return from_cases(tags, function_name, function, test_cases)

def from_cases_with_tags(tags):
    return partial(from_cases, tags)

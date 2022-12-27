import unittest
from fununit import TestCase, TestSuite
from fununit import adapters

def multiply(a, b):
    return a * b

def to_lower(string):
    return string.lower()

multiply_tests = TestSuite.from_cases(
    suite_name = "Multiply",
    function_name = "multiply",
    function = multiply,
    test_cases = [
        TestCase.create(
            case_name = "identity",
            parameters = [1, 2],
            expected = 2),
        TestCase.create(
            case_name = "normal_case",
            parameters = [3, 4],
            expected = 12),
        TestCase.create(
            case_name = "zero",
            parameters = [0, 6],
            expected = 0),
    ])

to_lower_tests = TestSuite.from_cases(
    suite_name = "ToLower",
    function_name = "to_lower",
    function = to_lower,
    test_cases = [
        TestCase.create(
            case_name = "empty_string",
            parameters = [""],
            expected = ""),
        TestCase.create(
            case_name = "already_lower",
            parameters = ["hello world"],
            expected = "hello world"),
        TestCase.create(
            case_name = "normal_case",
            parameters = ["Hello World"],
            expected = "hello world"),
    ])

all_tests = adapters.unittest.build_load_bundle_suites(
    [to_lower_tests,
    multiply_tests,
    ])
unittest.TextTestRunner(verbosity=2).run(all_tests)

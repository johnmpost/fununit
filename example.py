import unittest
from fununit import TestCase, UnitTest, TestResult
from fununit.run import run_tests

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

tags = ["Math"]

multiply_tests = UnitTest.from_cases(
    tags = tags,
    function_name = "multiply",
    function = multiply,
    test_cases = [
        TestCase.create(
            case_name = "identity",
            parameters = (1, 2),
            expected = 2),
        TestCase.create(
            case_name = "zero",
            parameters = [0, 6],
            expected = 0),
        TestCase.create(
            case_name = "positive",
            parameters = { "a": 3, "b": 4 },
            expected = 12),
    ])

add_tests = UnitTest.from_cases(
    tags, "add", add, [
        TestCase.create("zero", (0, 0), 0),
        TestCase.create("positive", (1, 2), 3),
        TestCase.create("negative", (-1, -2), -3),
        TestCase.create("mixed", (1, -2), -1),
    ])

run_tests(multiply_tests + add_tests)

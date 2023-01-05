import unittest
from fununit import TestCase, UnitTest
from fununit import adapters

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

tags = ["Math"]

multiply_tests = UnitTest.many_from_cases(
    tags = tags,
    function_name = "multiply",
    function = multiply,
    test_cases = [
        TestCase.create(
            case_name = "identity",
            parameters = (1, 2),
            expected = 2),
        TestCase.create(
            case_name = "normal_case",
            parameters = (3, 4),
            expected = 12),
        TestCase.create(
            case_name = "zero",
            parameters = (0, 6),
            expected = 0),
    ])

add_tests = UnitTest.many_from_cases(
    tags, "add", add, [
        TestCase.create("zero", (0, 0), 0),
        TestCase.create("positive", (1, 2), 3),
        TestCase.create("negative", (-1, -2), -3),
        TestCase.create("mix", (1, -2), -1),
    ])

import unittest
from fununit import TestCase, UnitTest
from fununit import adapters

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
            parameters = (1, 2),
            expected = 2,
            case_name = "identity"),
        TestCase.create(
            parameters = (0, 6),
            expected = 0,
            case_name = "zero"),
        TestCase.create(
            parameters = (3, 4),
            expected = 12),
    ])

add_tests = UnitTest.from_cases(
    tags, "add", add, [
        TestCase.create((0, 0), 0, "zero"),
        TestCase.create((1, 2), 3, "positive"),
        TestCase.create((-1, -2), -3, "negative"),
        TestCase.create((1, -2), -1, "mixed"),
    ])

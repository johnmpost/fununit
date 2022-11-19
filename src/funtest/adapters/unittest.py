import unittest

def build_test(unit_test):
    result = unit_test.function(*(unit_test.parameters))
    def test(self):
        getattr(self, "assertEqual")(unit_test.expected, result)
    return test

def get_test_name(unit_test):
    return f"test_{unit_test.function_name}_{unit_test.case_name}"

def build_suite(test_suite):
    suite_name = f"Test{test_suite.suite_name}"
    base_classes = (unittest.TestCase, )
    unit_tests = {
        get_test_name(unit_test)
        : build_test(unit_test)
        for unit_test in test_suite.unit_tests }
    built_suite = type(suite_name, base_classes, unit_tests)
    built_suite.__module__ = ""
    return built_suite

def build_load_bundle_suites(test_suites):
    loader = unittest.TestLoader()
    built_loaded_suites = [
        loader.loadTestsFromTestCase(
        build_suite(test_suite))
        for test_suite in test_suites ]
    bundled = unittest.TestSuite(built_loaded_suites)
    return bundled

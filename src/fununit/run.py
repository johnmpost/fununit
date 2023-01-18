from fununit import TestResult
from fununit.utils import show_list
from functools import partial

def show_result(test_result):
    return f"{test_result.function_name}, {test_result.case_name}, {test_result.expected}, {test_result.actual}, {test_result.passed}"

def run_tests_custom_batch(show_results_fn, unit_tests):
    results = TestResult.from_tests(unit_tests)
    shown_results = show_results_fn(results)
    print(shown_results)

def run_tests_custom_single(show_result_fn, unit_tests):
    def show_results_fn(results):
        shown_results = [show_result_fn(result) for result in results]
        return show_list(shown_results)
    run_tests_custom_batch(show_results_fn, unit_tests)

run_tests = partial(run_tests_custom_single, show_result)

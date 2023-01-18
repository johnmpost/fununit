from fununit import TestResult
from fununit.utils import show_list
from functools import partial

def show_tags(tags):
    return f"[{', '.join(tags)}]"

def passed_to_string(did_pass):
    return "PASSED" if did_pass else "FAILED"

def show_passed_result(result):
    return f"{passed_to_string(result.passed)} {show_tags(result.tags)} {result.function_name}.{result.case_name}"

def show_result(test_result):
    # TODO: when failed, show details on parameters, expected, and actual
    return show_passed_result(test_result)

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

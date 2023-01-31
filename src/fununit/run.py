from fununit import TestResult
from fununit._utils import _show_list
from functools import partial
from fununit._utils import _indent_lines

def _show_tags(tags):
    return f"[{', '.join(tags)}]"

def _passed_to_string(did_pass):
    return "PASSED" if did_pass else "FAILED"

def _show_passed_result(result):
    return f"{_passed_to_string(result.passed)} {_show_tags(result.tags)} {result.function_name}.{result.case_name}"

def _show_failed_result(result):
    summary = f"{_passed_to_string(result.passed)} {_show_tags(result.tags)} {result.function_name}.{result.case_name}"
    detail = f"parameters = {result.parameters}\nexpected = {result.expected}\nactual = {result.actual}"
    indented_detail = _indent_lines(4, detail)
    return f"{summary}\n{indented_detail}"

def _show_result(test_result):
    return _show_passed_result(test_result) if test_result.passed \
        else _show_failed_result(test_result)

def run_tests_batch_display(show_results_fn, unit_tests):
    """
    Runs the given unit_tests, use if you want full control of what is shown given a list of TestResult 
    """
    results = TestResult.from_tests(unit_tests)
    shown_results = show_results_fn(results)
    print(shown_results)

def run_tests_list_display(show_result_fn, unit_tests):
    """
    Runs the given unit_tests, use if you want to specify how each single TestResult should be shown
    """
    def show_results_fn(results):
        shown_results = [show_result_fn(result) for result in results]
        return _show_list(shown_results)
    run_tests_batch_display(show_results_fn, unit_tests)

run_tests = partial(run_tests_list_display, _show_result)


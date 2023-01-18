from fununit import TestResult

def show(test_result):
    return f"{test_result.function_name}, {test_result.case_name}, {test_result.expected}, {test_result.actual}, {test_result.passed}"

def show_many(test_results):
    shown_results = [show(test_result) for test_result in test_results]
    return show_list(shown_results)

def run_tests(unit_tests):
    results = TestResult.from_tests(unit_tests)
    shown_results = show_many(results)
    print(shown_results)

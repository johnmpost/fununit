# Introduction

`fununit` ("**fun**ctional **unit** testing") is a functional, declarative unit-testing library for testing pure functions in Python.

Here are some key features:

- functional
  - fununit is built for testing pure functions
  - fununit has a functional API, incorporating higher-order and pure functions
- declarative
  - fununit lets you describe unit tests in a fully declarative manner
- removes testing boilerplate
  - fununit removes unnecessary code duplication between tests
  - this makes tests more maintainable - and more fun to write ;)

# Installation

You can install fununit from PyPI:

`pip install fununit`

# Basic Usage

Due to its API being made up of pure functions, fununit is very flexible. You can customize almost any part of it, including making any testing flow you could want. Despite that, it's easy to get started with, using a basic testing flow.

Remember, fununit is for testing pure functions. Let's use this one as a simple example:

```python
def multiply(a, b):
    return a * b
```

So, we want to create unit tests for this function. But, unit tests start with test cases, so I'll cover those first.

Fununit provides a type called `TestCase`. A `TestCase` has three properties:

- `case_name`, the name of the test case
- `parameters`, the parameters that define the test case
- `expected`, the value you expect given those parameters

Use the `TestCase.create` function to create test cases:

```python
TestCase.create("zero", (0, 6), 0)
TestCase.create("identity", (1, 2), 2)
TestCase.create("positive", (3, 4), 12)
```

Then, we can turn those test cases into unit tests. The `UnitTest` type has six properties that we care about:

- `tags`, you can tag unit tests with anything you want, for example, the module name
- `function_name`, the name of the function being tested
- `function`, the function itself
- the same three as `TestCase`: `case_name`, `parameters`, and `expected`

As you can see, a `UnitTest` is just a `TestCase` with some extra information. This means we can take our test cases and make them into full unit tests. The normal way to do this is using the `UnitTest.from_cases` function.

Let's do that. We'll pass in a list of tags (in this case, showing that this function is part of our Math module), the name of the function, and the function itself. Then, we give it the list of test cases we want to have.

```python
from fununit import TestCase, UnitTest

multiply_tests = UnitTest.from_cases(
    ["Math"], "multiply", multiply, [
        TestCase.create("zero", (0, 6), 0)
        TestCase.create("identity", (1, 2), 2)
        TestCase.create("positive", (3, 4), 12)
    ])
```

And now we have a full set of unit tests for the multiply function, described using fununit. The easiest way to run them is to use the default test runner:

```python
from fununit.run import run_tests

run_tests(multiply_tests)
```

The console output of the default test runner looks like this (with a failing case for demonstration):

```
PASSED [Math] multiply.zero
PASSED [Math] multiply.identity
PASSED [Math] multiply.positive
FAILED [Math] multiply.negative
```

Check out example.py and the advanced usage section for more.

# Advanced

## Usage

- explanation of some advanced functions
- ideas for non-basic testing patterns
- ideas for non-basic testing flows

## Advantages of fununit

- how writing tests is better
- it's not just what writing tests looks like
- laundry list

- **Functional Approach:** fununit is based on functional programming concepts, which allows for a more modular, composable and reusable way of writing and structuring tests. This can make it easier to understand and maintain the test codebase.
- **Declarative Testing:** fununit's approach is fully declarative, which allows the user to expressively describe the tests that they want, not how they should be run.
- **Test Case Management:** fununit allows for better management of test cases, as it lets the user isolate the them. This allows for better organization and reusability of test cases.
- **Test Result Management:** fununit allows for better management of test results, as it explicitly treats test results as their own type. This allows for better organization and analysis of test results.
- **Flexible Test Reporting:** fununit allows full control over the test reporting process, which can be useful for customizing the results display, generating reports in different formats, or integrating with other tools.
- **Custom Test Runners:** fununit makes it easy to make custom test runners, which can be useful for adapting the test execution process to specific needs. This can be useful for adding custom logic or hooks for test execution.
- **Programmatic Control of Test Execution:** fununit allows for programmatic control over the test execution process. This means that users have full control over when, how, and which tests are run.
- **Test Structure:** fununit provides a clear and novel structure for the entire unit testing process. It is rigid in all the right ways, and flexible and extensible in every other way. With fununit, you of course get all the built-in functions, but those are just the groundwork for a brand new way of thinking about unit testing. You get to decide where you take these ideas, whether that's building cool things on top of fununit's core, or rewriting almost everything to make it even better. (If you decide to do that, consider contributing!)

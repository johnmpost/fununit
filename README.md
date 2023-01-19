# Introduction

`fununit` ("**fun**ctional **unit** testing") is a functional, declarative unit-testing library for testing pure functions in Python.

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

And now we have a full set of unit tests for the multiply function, written using fununit. The easiest way to run them is to use the default test runner:

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

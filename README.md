# Introduction

`fununit` ("**fun**ctional **unit** testing") is a functional, declarative unit-testing library for testing pure functions in Python.

Here are some key features:

- **functional:** fununit has a functional API, which means it has great composability and flexibility
- **declarative:** fununit lets you describe unit tests in a fully declarative manner
- **cuts out all code duplication:** fununit removes up to 100% of unnecessary code duplication between tests

All of this makes tests more maintainable - and more fun to write ;)

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

Let's do that. We'll pass in a list of tags (in this case, one tag to show that this function is part of our Math module), the name of the function, and the function itself. Then, we give it the list of test cases we want to have.

```python
from fununit import TestCase, UnitTest

multiply_tests = UnitTest.from_cases(
    ["Math"], "multiply", multiply, [
        TestCase.create("zero", (0, 6), 0),
        TestCase.create("identity", (1, 2), 2),
        TestCase.create("positive", (3, 4), 12)
    ])
```

Note: You may like having `TestCase.create` for each test case, as it is very explicit about what you are creating. However, fununit has a more implicit, less verbose approach if you prefer it. This example uses the `UnitTest.from_cases_implicit` function, and even imports it as `tests` for some very succinct code.

```python
from fununit.UnitTest import from_cases_implicit as tests

multiply_tests = tests(
    ["Math"], "multiply", multiply, [
        ("zero", (0, 6), 0),
        ("identity", (1, 2), 2),
        ("positive", (3, 4), 12)
    ])
```

Whichever format you choose, we now have a finished set of unit tests for the multiply function, described using fununit. The easiest way to run them is to use the default test runner:

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

# Advanced Usage

- explanation of some advanced functions
- levels of verbosity that you can do
- ideas for non-basic testing patterns
- ideas for non-basic testing flows
- explanation of equality function property of UnitTest

# Advantages of fununit

## Writing Tests

If you were to compare fununit to another testing framework in terms of functionality offered and how you describe tests, a close comparison would be pytest with parametrize, as both do parameterized testing. I'll do a side-by-side comparison.

### pytest with parametrize:
![pytest tests with comparison highlights](assets/pytest.png)

### fununit (using succinct style explained above):
![fununit tests with comparison highlights](assets/fununit.png)

There are many common elements between the two (regardless of structure of the elements):
| Element | pytest and parametrize | fununit |
| --- | --- | --- |
| Named group of separate functions being tested together | `test_math.py` is the name of the file/module where `test_multiply` is defined | `"Math"` is a tag in a parameter to `UnitTest.from_cases` |
| Name of the function being tested | `test_multiply` is the name of the test function | `"multiply"` is a parameter to `UnitTest.from_cases` |
| Function being tested | `multiply` is called directly with parameters in the `assert` statement | `multiply` is a parameter to `UnitTest.from_cases` |
| Parameters of each test case | the `a` and `b` elements of each 3-tuple given to `@pytest.mark.parametrize` | the elements of the second parameter to each `TestCase.create` |
| Expected result of each test case | the `result` element of each 3-tuple given to `@pytest.mark.parametrize` | the third parameter to each `TestCase.create` |

There is one glaring uncommon element: fununit test cases are required to have a name.

And there are plenty of structural differences in how those common elements are laid out, which is where fununit really shines.

- With pytest, you write "a," "b," and "result" three separate times. Fununit's abstraction is designed around this style of testing, so you write them zero times.
- With pytest, you need to write an imperative `assert` statement. Granted, it is a very simple statement. However, it is still less composable than the expressions that fununit uses.  
- Pytest is syntax-heavy. You have a decorator, you need to define a new function using the `def` keyword, you need to use the `==` operator and the `assert` keyword. Fununit just has functions and values, which improves combosability.
- Pytest has (relatively) a lot of redundancy and repetition. Every test you write will need the parametrize decorator, and you'll need to define a test function with an assert statement in it. With fununit, you have the option to cut out all unnecessary repetition, and only provide the things that actually matter for each unit test.

These advantages are nuanced, to be sure. There's nothing wrong with pytest's parametrize, in fact it is actually pretty nice. But unit testing is so common that I think it is worth it to take something pretty good and improve that last little bit.

All in all, in terms of writing tests, the main benefit that fununit offers comes down to a moderately higher level of abstraction.

## More Than Writing Tests

it's about the entire fununit philosophy and extensible api, not just the standard way of writing tests. these things also offer benefits

## Laundry List

- **Functional Approach:** fununit is based on functional programming concepts, which allows for a more modular, composable and reusable way of writing and structuring tests. This can make it easier to understand and maintain the test codebase.
- **Declarative Testing:** fununit's approach is fully declarative, which allows the user to expressively describe the tests that they want, not how they should be run.
- **Test Case Management:** fununit allows for better management of test cases, as it lets the user isolate the them. This allows for better organization and reusability of test cases.
- **Test Result Management:** fununit allows for better management of test results, as it explicitly treats test results as their own type. This allows for better organization and analysis of test results.
- **Flexible Test Reporting:** fununit allows full control over the test reporting process, which can be useful for customizing the results display, generating reports in different formats, or integrating with other tools.
- **Custom Test Runners:** fununit makes it easy to make custom test runners, which can be useful for adapting the test execution process to specific needs. This can be useful for adding custom logic or hooks for test execution.
- **Programmatic Control of Test Execution:** fununit allows for programmatic control over the test execution process. This means that users have full control over when, how, and which tests are run.
- **Test Structure:** fununit provides a clear and novel structure for the entire unit testing process. It is rigid in all the right ways, and flexible and extensible in every other way. With fununit, you of course get all the built-in functions, but those are just the groundwork for a brand new way of thinking about unit testing. You get to decide where you take these ideas, whether that's building cool things on top of fununit's core, or rewriting almost everything to make it even better. (If you decide to do that, consider contributing!)

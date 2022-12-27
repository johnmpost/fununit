# fununit

`fununit` ("**fun**ctional **unit** testing") is a functional, declarative, unit-testing library for testing pure functions in Python. It has the following characteristics:

- functional
  - fununit makes use of functional programming ideas such as higher-order functions and pure functions
  - in fact, its core purpose is to test pure functions
  - the fununit API exposes a selection of pure functions, allowing for great flexibility with their use
- declarative
  - fununit allows you to describe the tests you want to run in a declarative manner
  - expressively describe the tests that you want, not how they should be run
- removes boilerplate testing code
  - drastically reduces code duplication between tests, improving maintainability
  - allows for writing very succinct code, making it faster and easier to write and read
- framework-agnostic
  - fununit is not coupled with any particular testing framework
  - rather, it has adapters to translate fununit tests into any other format
  - currently, there is an adapter for the built-in `unittest` module, which works great with fununit
  - if you have specific requirements, feel free to write you own custom adapter

fununit is a library to test pure functions. Take a look at `example.py` to see fununit being used. Because the API is very flexible, you can extend and build its simple functions into a custom flow if you want. But, here is the standard approach to writing tests with fununit:

  - Create a `Suite` for testing a particular function. 
  - For each suite, specify a name for the suite, a name for the function being tested, and the function itself being tested.
  - Also specify a list of `Cases`. Each case has a name, a list of parameters to pass to the function, and the expected return value.
  - As shown in the example, `Suites` and `Cases` are created using constructor functions from their respective modules. You may choose to use keyword args instead of positional args to make your tests more explicit.

A note about the fununit domain:

  - `UnitTest` is the basic type. It contains everything needed to describe a single unit test in isolation, and nothing more.
  - `TestCase` is a `UnitTest` that is partially built. It is missing some attributes. A `TestCase` on its own does not represent a standalone unit test. However, a group of them, paired with only one set of the missing attributes, is useful for describing several test cases without redundantly repeating the information about the function being tested.
  - `TestSuite` is nothing but a group of `UnitTests` with a name. However, it has a constructor function that allows building one to test a particular function against a list of cases.

This is the fununit way of describing your unit tests. It allows you to dig way down deep into the core of what constitutes a unit test. You only specify what actually matters for each test, nothing more.

Finally, to actually run your fununit-notated unit tests, use an adapter module. For example, the `adapters.unittest` has 2 useful functions. `build_suite` builds a fununit `TestSuite` into a `unittest.TestCase`. You can then use it how you would any other object of that type. `build_load_bundle_suites` takes a list of fununit `TestSuites`, builds them as above, then transforms them via `loading` and `bundling` into a `unittest.TestSuite`. It can then be run using any `TestRunner` provided by `unittest`. Every unit test / test case notated with fununit will be run as a separate unit test by `unittest`, so you will be able to immediately see particular cases in a suite, if any, that have failed.

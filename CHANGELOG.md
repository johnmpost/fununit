# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2023-01-30

### Changed

- the default test runner now displays extra details on a failed test

## [2.0.0] - 2023-01-24

### Changed

- fununit is no longer based on adapters to other unit-testing libraries

### Added

- `TestResult` type
- the `run` module for basic test running functions
- `tags` and `equality_fn` properties to `UnitTest`
- a default equality function

### Removed

- `TestSuite` type
- `unittest` adapter

## [1.0.0] - 2022-12-27

### Added

- core api
- adapter for `unittest` module
- example.py
- readme
- this changelog
- license file
- how to contribute
- build info for PyPI

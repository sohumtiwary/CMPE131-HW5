# CMPE131-HW5

# Homework
- Name: Sohum Tiwary
## Question 1) Define the following unit, integration, regression tests and when you would use each?
- Unit test: A unit test verifies a small isolated piece of code, a module, for example, and uses no external resources. It is to validate individual functions early and catch logic errors before integration.
- Integration test: An integration test is to check how multiple modules or components work together. This is used after unit tests to verify system-level behavior.
- Regression test: A regression test is written after a bug is found to prove that the issue is fixed for future versions. It locks in the correct behavior and prevents the same defect from reappearing.
## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.
A Pytest discovery finds and runs tests in files with names that start with test_ or end with _test
Inside the files, any function or class method is recognized and executed as a test.
A fixture in pytest is a reusable setup/teardown function that provides resources or state to tests.

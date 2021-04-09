<h3>Pylint and Coverage</h3>

<h5>Why do we use it?</h5>

Pylint is a static analysis tool which may produce alot of useful errors and warning which may help us catch bugs, but it also containts many "opinionated" assumptions about how your code should look, but those can be easily overrided and disabled. Some minor issues is that for major projects like this one, you need to consistently run pylint since the start or otherwise the output would be enormous. This process may be a bit tedious but will prevent some bugs which will be useful in the future. 

Coverage.py measures code coverage, typically during test execution. It uses code analysis tools provided in the Python standard library to determine which lines are executable, and which have been executed. We do this so that we can ensure that our code is running correctly and that our test cases cover all the branches. This may be useful in finding bugs e.g. in the leap year example, and may save you a lot of time. This will generate a report and give you a percentage of the number of lines which have been executed by your tests. 

e.g. 

![Coverage Report]
(https://ibb.co/5MtNdGR)

<h5>Is this enough to show that your backend works perfectly with your frontend?</h5>

**NO.** Remember that pylint and coverage are just tests and that even if we have perfect coverage, 10/10 pylint score, it doesn't mean that our code is perfect and that there are no errors. There is no way to fully validate and verify software development with just these tests. Instead, we can let our users play around with it and see if they have any issues or find any bugs.  
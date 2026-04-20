# CS50P - Introduction to Programming with Python

## notes: Lecture 5 - Unit Tests
+ original notes: [course site](https://cs50.harvard.edu/python/notes/5/)

### UNIT TESTS
+ it is common to write program to test your program
+ the test programs can not test everything
+ therefore, representative values must be tested with potential corner cases (!!!)
+ keep the test program nice, simple, and small
+ following the convention, a test program is named test_\<programm name>.py, e.g. for calculator.py the test program is called tets_calculator.py
```python
#calulator.py
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n + n #bug, n * n is the fix

if __name__ == "__main__":
    main()
```
```python
#test_calculator.py
from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
```
+ however, in this example only 2 cases are tested with 4 lines of code and corner cases are missing

### ASSERT
+ the keyword assert checks if assertions are True
+ if the assertion is True, the code is passed
+ if the assertion is False, a AssertionError is raised, e.g.

```python
from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()
```
+ assert can be combined with try and except, e.g.
```python
from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")

if __name__ == "__main__":
    main()
```

### PYTEST
+ pytest is a third-party library, which allows to automate unit testing (testing of individual units/functions of your code) 
+ pytest can be installed by pip (pip install pytest)
+ for pytest, the test program must be modified (main function removed), e.g.
```python
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
```
+ for testing pytest \<test program name>.py is typed in the terminal
+ then, the test program is tested and a report containing clues is returned , e.g.
```
=============================================== test session starts ===============================================
platform
rootdir
collected 1 item                                                                                                    

test_calculator.py F                                                                                         [100%]

==================================================== FAILURES ===================================================== 
___________________________________________________ test_square ___________________________________________________ 

    def test_square():
        assert square(2) == 4
>       assert square(3) == 9
E       assert 6 == 9
E        +  where 6 = square(3)

test_calculator.py:5: AssertionError
============================================= short test summary info =============================================
FAILED test_calculator.py::test_square - assert 6 == 9
================================================ 1 failed in 0.12s ================================================
```
+ the testing of the function is stopped when an error arises -> after the break, further asserts are not tested, e.g. in the example above after testing square(3), test_square() is stopped due to an error and square(-2), square(-3), and square(0) are not tested anymore
+ in the line with the test program name either F (test failed) or "." (test passed) is written as brief conclusion
+ in general, representative testing values are splitted in different groups of tests (every test is a function) to get a better overview of the bugs, e.g.
```python
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
```
+ the corresponding pytest report
```
================================================================================================== test session starts ===================================================================================================
platform
rootdir
collected 3 items                                                                                                                                                                                                         

test_calculator.py FF.                                                                                                                                                                                              [100%]

======================================================================================================== FAILURES ========================================================================================================
_____________________________________________________________________________________________________ test_positive ______________________________________________________________________________________________________

    def test_positive():
        assert square(2) == 4
>       assert square(3) == 9
E       assert 6 == 9
E        +  where 6 = square(3)

test_calculator.py:5: AssertionError
_____________________________________________________________________________________________________ test_negative ______________________________________________________________________________________________________

    def test_negative():
>       assert square(-2) == 4
E       assert -4 == 4
E        +  where -4 = square(-2)

test_calculator.py:9: AssertionError
================================================================================================ short test summary info ================================================================================================= 
FAILED test_calculator.py::test_positive - assert 6 == 9
FAILED test_calculator.py::test_negative - assert -4 == 4
============================================================================================== 2 failed, 1 passed in 0.11s ===============================================================================================
```
+ when an error arises, testing of the function is stopped (as described above) and the next function is tested
+ in the line with the test program name, the brief conclusion is shown again -> FF. (first function failed, second function failed, third function passed)
+ instead of assert, the functions pytest.raises() with the with statement can be used for expected errors, e.g.
```python
  import pytest

  from calculator import square

  def test_positive():
      assert square(2) == 4
      assert square(3) == 9

  def test_negative():
      assert square(-2) == 4
      assert square(-3) == 9

  def test_zero():
      assert square(0) == 0

  def test_str():
      with pytest.raises(TypeError):
          square("cat")
```
+ the with statement simplifies resource management by automatically handling setup and cleanup, ensuring files or connections close safely even if errors occur
+ since float values cannot be represented precise (floating-point precision), their comparison by assert is more challenging
+ the function pytest.approx(i, abs = j) can help to test floats, comparison of two values within the tolerance abs -> abs(float-i) < abs
```python
  import pytest

  from calculator import square

  def test_positivefloat():
      assert square(1.67) == pytest.approx(2.78, abs=0.01)

```
+ the tolerance must be determined regarding to the corresponding requirements

### TESTING STRINGS
+ the testing of strings is analogue to the testing of integers, e.g.
```python
#hello.py
def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
```
```python
#test_hello.py
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"
```
+ side effects can not bet tested; a return value is needed for testing-> in general, side effects are avoided in functions and return values are used
+ the following code cannot be tested because hello() has no return value
```python
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

if __name__ == "__main__":
    main()
```

### ORGANIZING TESTS INTO FOLDERS
+ in unit testing, multiple test programs are common
+ therefore, all test programs are placed in the folder test (common convention), e.g.
```
├── test
│   ├── __init__.py
│   ├── test_file_1.py
│   └── test_file_2.py
└── file.py
```
+ the \_\_init\_\_.py file is required to treat the directory containing the files as package
+ by typing pytest test in the terminal, all test programs in the test folder are tested

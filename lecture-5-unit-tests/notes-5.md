# CS50P - Introduction to Programming with Python

## notes: Lecture 5 - Unit Tests
+ original notes: [course site](https://cs50.harvard.edu/python/notes/5/)

### UNIT TESTS
+ common to write programm to test your programm
+ corner cases!!!
+ dont test everything but representives (potential cornercases) -> nice and simple and small
+ convention: test_<programm name\>.py, e.g.

### ASSERT
+ keywords
+ AssertionError -> not user-friendly -> try except

### PYTEST
+ pytest third party library? allows to automate the testing of your code
+ unit testing -> testing indiviudal units of your code -> functions

+ assert key words
+ no main necessry
+ pytest test_calculator.py in terminal -> stops as first error in every test function and gives you a clue

+ split tests into different groups
+ FF. (dot means pass)

+ float values -> floating points inprecision (decimal points can not  be represented precise ) -> pytest.approx()/  pytest.approx(i, abs= j) tolereance +- j

+ with pytest.raises -> context manager

### TESTING STRINGS
+ ' " + esccaping
+ 1e-2

+ side effects will be not tested; return value needed -> in general side effects are avoided and with return values is worked

### Organizing TESTS into Folders

__init__.py -> treat that folder as an package 
pytest test



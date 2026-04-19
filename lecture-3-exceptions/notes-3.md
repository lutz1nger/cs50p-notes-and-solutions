# CS50P - Introduction to Programming with Python

## notes: Lecture 3 - Exceptions
+ original notes: [course site](https://cs50.harvard.edu/python/notes/3/)

### EXCEPTIONS
+ exceptions are problems or erros in a code

### SYNTAX ERROR
+ arises when syntax/rules of python are not followed resulting in not starting of the code, e.g. 
```python
print("hello world) # output: SyntaxError: unterminated string literal
```
+ syntax erros can be fixed easily by the programmer

### RUNTIME ERROR
+ arises while a code is running reuslting in a interruption of the code
+ some common errors:

| error | description |
| --- | --- |
| ValueError | incorrect value type |
| NameError | missing variable, function, module, etc. |
| MemoryError | code uses more memory as available |
| KeyError | missing key in a dict |

### ERROR HANDLING
+ try and except are keywords, check if an error occurs and therefore, the code is not interrupted, e.g.
```python
try:
    x = int(input("What's x?")) # output when no error occurs
    print(f"x is {x}") # output when no error occurs
except ValueError:
    print("x is not an integer") # output when an error occurs
```
+ for the keyword statement, the errors should be known and you must be specific with the exceptions; for multiple error types multiple excepts are necessary
+ for best practice, only the lines, which can fail, should be used in the try statement (it is more pythonic), e.g.
```python
try:
    x = int(input("What's x?")) # only this line can fail
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
+  however, in this example we will get an NameError, when no integer is in the input resulting that x is not assigned due to a ValueError
+  therefore, the try and except statements can be combined with the else statement, e.g.
```python
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
+ Improving the code with a while True loop:
```python
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```
+ instead of break, return can be used
```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()
```
+ further improvements:
```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()
```
+ since the variable x is used only once, the input can be returned directly and x can be avoided
+ in general, unnecessary variables should be avoided
```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            print("x is not an integer")


main()
```

### PASS
+ pass statement is a placeholder performing a null operation (returns nothing when executed), e.g.
```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass # output is nothing


main()
```  
+ for a more reusable and dynamic code, the prompt is insert in the main(); therefore, get_int() can be used in other codes/programms
```python
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
```

### RAISE
+ the raise is used to activate an exception, e.g.
```python
x = -1
if x < 0:
  raise Exception()
```
+ generic error: Exception()
+ inside the brackets an error message can be added, e.g.
```python
x = -1
if x < 0:
  raise Exception("No negative numbers!")
```
+ further runtime error can be used, e.g.
```python
x = -1
if x < 0:
  raise ValueError("No negative numbers!")
```

### DEBUGGING
+ for the idendification of bugs, the most interpreter/editior have a build-in debugger
+ in VS Code it is called 'run and debug' (symbol with play button and bug)
+ for debugging:
  
    1\. set an breakpoint in a code line (red dot on the left side of code line number)  
    2\. start the debugger  
    3. at the breakpoint the code is stopped and then you examine the every code line with the functions 'continue' (go to the next breakpoint), 'step over' (go to the next code line), 'step into' (go into the function), and 'step out' (leave a function)

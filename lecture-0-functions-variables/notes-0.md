# CS50P - Introduction to Programming with Python

## notes: Lecture 0 - Functions, Variables
+ original notes: [course site](https://cs50.harvard.edu/python/notes/0/)

### COMMENTS
+ inside a code comments can be made using "#" for e.g. documentation or to-dos

### FUNCTIONS
+ commands performing actions - called **SIDE EFFECTS**; e.g. print()
```python
print() #prints input on the screen or display
print("hello" + "world") #output: helloworld
print("hello", "world") #output: hello world
```
+ inside parantheses is the input - called **ARGUMENTS**

+ **CHECK ALWAYS THE FUNCTION DOCUMENTATION!!!**
e.g. for print():
```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
#asterik(*) before objects means that multiple arguments can be used as input
#default seperation is a whitespace (sep=' '), default end is a new line (end='\n')
```
+ objects, sep, end, ... are called **PARAMETERS** -> difference arguments and parameters: parameters are defined in the function definition and arguments are values being passed to the function

### VARIABLES
+ values can be assigned using "=", e.g.
```python
name = "David"
```
+ multiple values can be assigned in one line, e.g.
```python
name = "David Malan"              
first_name, last_name = name.split(" ") #output: first_name is "David" and last_name is "Malan"
```

### STR
+ string variable -> text
+ string variables are in either single (') or double quotation marks ("), e.g.
```python
name = "David Malan"

name = 'David Malan'
```
+ for consistency use only one type of quotation marks in the code
+ triple quotation marks (''' or """) are used for multi-line strings including line break, e.g.
```python
text = """first line,
second line,
third line"""

text = '''first line,
second line,
third line'''
```
+ to use a quotation marks in a string, Escaping must can be used by backslash (\), e.g.
```python
name = "\"David\"" #output: "David"
```
+ str can be modifided by **STRING-METHODS**, e.g.
```python
str.strip() #whitspaces from the left and right of the variable are removed
```
+ string-methdos can be chained multiple times, e.g.
```python
str.strip().title() #whitspaces from the left and right of the variable are removed and the first letter of every word is capitalized
```

### F STRING
+ formatting string, e.g.
```python
f_string = f"hello, {name}" #the f indidactes it is a f string and therefore, the variable name is used in this string
```

### INT
+ int variable -> integers
+ can be used with e.g.  +, -, *, /, and % operators; in python % is the modulo parameter (return remainder of a division, e.g. 4%2 = 0 and 5%2 = 1)
+ function int() can be used to convert variable into int variable

### FLOAT
+ float variable -> floating-point number
+ for very small or large numbers the scientific notation (1e\<number>) can be used, e.g.
```python
number1 = 1e5 #output: 100000
number2 = 1e-5 #output: 0.00001
```
+ function float() can be used to convert variable into float variable
+ float can be rounded by the function round() -> documentation: round(number\[, ndigits]) -> in documentations [] means the argument is optional
+ f string for float:
```python
float = f"{z:.2f}" #variable z is separated by a decimal point and has two decimal places
```

### DEF
+ own function can be created with the def function:
```python
def squared(x): #a function 'squared' is defined with the parameter x
  y = x*x #side effect, but this values are not returned by the function
  return y #RETURN VALUE
```         
+ parameters are optional (e.g. def squared():)
+ default values can be added to the parameters (e.g. def squared(x=3):)
+ in general, parameters are only valid in the SCOPE of the def function.
+ value returned by the function is called **RETURN VALUE**
+ the RETURN VALUE is optional
+ global variables can be changed inside a def function by use of the prefix 'global', e.g.:
```python
x = 2
def multiple(y):
  global x
  result1 = y + x #here is x = 2 as defined
  x = 3 #here x gets 3 as assigned
  result2 = y + x
  return result1, result2             
```           
+ def must be defined before used in the code, therefore, one option is to work with a main code:
```python
def main(): #here the main code is written as def
  ....
  
def function1(): #then other functions are defined below teh main code
  ....

main() #main code is executed
```

### COMMANDS IN THE TERMINAL
| commands | description |
| --- | --- |
| code <file.py> | create new code file<file.py> |
| ls | list of all files in the current directory |
| cp <file> <dir> | copy file <file> into the directroy <dir> |
| mv <file> <dir> | move file <file> into the directroy <dir> |
| rm <file> | delete file <file> |
| mkdir <dir> | create new directory <dir> |
| cd | change to root directory |
| cd .. | change to directory one level of the directory tree up |
| cd <dir> | change to directory <dir> |
| rmdir <dir> | delete directory <dir> |
| clear | clear terminal|

# CS50P - Introduction to Programming with Python

## notes: Lecture 1 - Conditionals
+ original notes: [course site](https://cs50.harvard.edu/python/notes/1/)

### Bool
+ boolean variable -> can only be FALSE (0) or TRUE (1)  

### CONDITIONALS
+ conditionals allow your program to make decisions, choosing one path over another depending on specified conditions
+ return value of a condition is a boolean expression

### OPERATORS FOR CONDITIONALS
| operator | description |
| --- | --- |
| > | greater than |
| >= | greather than and equal to |
| < | less than |
| <= | less than and equal to |
| == | equals (note the double equal sign: a single equal sign assigns a value, whereas two equal signs compare values) |
| != | not equal to |

### IF STATMENT
+ allows your programm to decide whether or not to execute code regarding a condition
```python
x = int1 #x is an integer
y = int2 #y is an integer

if x < y: #if statement compares x and y and returns a boolean expression/bool
    print("x is less than y") #when the if statement is TRUE, the indented block is executed
```
+ alternative if not statement is possible as well, e.g.
```python
x = int1 #x is an integer
y = int2 #y is an integer

if not x == y: #if not statement compares if x is not equal to y
    print("x not equal to y") #when the if statement is TRUE, the indented block is executed
```
+ for a better control flow the elif statement and else statement can be used, e.g.
```python
x = int1 #x is an integer
y = int2 #y is an integer

if x < y: #if statement compares if x is less than y
    print("x is less than y") #when the if statement is TRUE, the indented block is executed
elif x > y: #elif stat statement compares if x is greater than y
    print("x is greater than y") #when the elif statement is TRUE, the indented block is executed
else:                                
    print("x is equal to y") #when the elif statement is FALSE, the indented block is executed
```
+ elif statement are only checked if the prior condition is FALSE, e.g. when in the code above the if statement is TRUE, the elif statement is not checked and skipped -> advantage: processing power is saved
+ else is only good when there are no other options you want to test for!!!

### OR
+ allows your program to decide between one or more alternatives, e.g.
```python
x = int1 #x is an integer
y = int2 #y is an integer

if x < y or x > y: #if statement compares if x is less than y or x is grateher than y
    print("x is not equal to y") #when the if statement is TRUE, the indented block is executed      
else:
    print("x is equal to y") #when the if statement is FALSE, the indented block is executed
```
+ here processing power can be saved by reversing the comparison:
```python
x = int1 #x is an integer
y = int2 #y is an integer

if x != y: #if statement compares if x is not equal to y
    print("x is not equal to y") #when the if statement is TRUE, the indented block is executed      
else:
    print("x is equal to y") #when the if statement is FALSE, the indented block is executed
```

### AND
+ analogue to OR, e.g.
```python
score = int1  #score is an integer  

if score >= 90 and score <= 100: #if statement compares if score is greather than and equal to 90 and score less than and equal to 100
    print("Grade: A") #when the if statement is TRUE, the indented block is executed      
elif score >=80 and score < 90: #elif statement compares if score is greather than and equal to 80 and score less than and equal to 90
    print("Grade: B") #when the elif statement is TRUE, the indented block is executed 
elif score >=70 and score < 80: #elif statement compares if score is greather than and equal to 70 and score less than and equal to 80
    print("Grade: C") #when the elif statement is TRUE, the indented block is executed 
elif score >=60 and score < 70: #elif statement compares if score is greather than and equal to 60 and score less than and equal to 70
    print("Grade: D") #when the elif statement is TRUE, the indented block is executed 
else:
    print("Grade: F") #when the elif statement is FALSE, the indented block is executed 
```
+ Python allows to chain conditions and operators, e.g. score >= 90 and score <= 100 -> 90 <= score <= 100
```python
if 90 <= score <= 100: #if statement compares if score is greather than and equal to 90 and score less than and equal to 100
    print("Grade: A") #when the if statement is TRUE, the indented block is executed      
elif 80 <= score < 90: #elif statement compares if score is greather than and equal to 80 and score less than and equal to 90
    print("Grade: B") #when the elif statement is TRUE, the indented block is executed 
elif 70 <= score < 80: #elif statement compares if score is greather than and equal to 70 and score less than and equal to 80
    print("Grade: C") #when the elif statement is TRUE, the indented block is executed 
elif 60 <= score < 70: #elif statement compares if score is greather than and equal to 60 and score less than and equal to 70
    print("Grade: D") #when the elif statement is TRUE, the indented block is executed 
else:
    print("Grade: F") #when the elif statement is FALSE, the indented block is executed 
```
+ further improvements
```python
score = int1 #score is an integer

if score >= 90: #if statement compares if score is greather than and equal to 90
    print("Grade: A") #when the if statement is TRUE, the indented block is executed      
elif score >= 80: #elif statement compares if score is greather than and equal to 80
    print("Grade: B") #when the elif statement is TRUE, the indented block is executed 
elif score >= 7: #elif statement compares if score is greather than and equal to 70
    print("Grade: C") #when the elif statement is TRUE, the indented block is executed 
elif score >= 60: #elif statement compares if score is greather than and equal to 60
    print("Grade: D") #when the elif statement is TRUE, the indented block is executed 
else:
    print("Grade: F") #when the elif statement is FALSE, the indented block is executed 
```

### RETURN VALUE IN FUNCTIONS
+ boolean expression can be used as return value in functions, e.g.
```python
def main():
    x = int1 #x is an integer
    if is_even(x): #TRUE or FALSE return value from the function is_even
        print("Even") #when the if statement is TRUE, the indented block is executed   
    else:
        print("Odd") #when the if statement is FALSE, the indented block is executed   

def is_even(n):
    if n % 2 == 0: #if statement compares if the modulo of n/2 is eual to 0
        return True #when the if statement is TRUE, the indented block is executed   
    else:
        return False #when the if statement is FALSE, the indented block is executed   

main()
```

### PYTHONIC
+ describes writing code that uses the design principles and idiomatic expressions of the Python programming language to make it elegant, readable, concise, and efficient, rather than following patterns from other languages, e.g.
```python

def main():
    x = int1 #x is an integer
    if is_even(x): #TRUE or FALSE return value from the function is_even
        print("Even") #when the if statement is TRUE, the indented block is executed   
    else:
        print("Odd") #when the if statement is FALSE, the indented block is executed

def is_even(n):
    return True if n % 2 == 0 else False #if statement compares if the modulo of n/2 is eual to 0 and return either TRUE or FALSE 
```
+ further improvements, because the if statement returns either TRUE or FALSE without an if statement
```python
def main():
    x = int1 #x is an integer
    if is_even(x): #TRUE or FALSE return value from the function is_even
        print("Even") #when the if statement is TRUE, the indented block is executed   
    else:
        print("Odd") #when the if statement is FALSE, the indented block is executed

def is_even(n):
    return n % 2 == 0 #if statement compares if the modulo of n/2 is eual to 0 and return either TRUE or FALSE
```
+ additional information: Python follows the same precedence rules for its mathematical operators that mathematics does. parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want.
+ Since expressions in parentheses are evaluated first!!!

### MATCH
+ match statement compares the value following the match keyword with each of the values following the case keywords
```python
  name = str1 #name is a string

  match name: #match statement for the variable name 
      case "Harry" | "Hermione" | "Ron":  # in match statement or is I -> similiar to if name == "Harry" or name == "Hermione" or name == "Ron": -> means that this cases occurs if name is equal to Harry or Hermione or Ron
          print("Gryffindor")                
      case "Draco": #this case occurs if name is equal to Draco
          print("Slytherin")
      case _: #in match statement else is underscore (_) -> this case occurs if name is not equal to all other cases -> meaning that name is not equal to Harry or Hermione or Ron or Draco
          print("Who?")
```

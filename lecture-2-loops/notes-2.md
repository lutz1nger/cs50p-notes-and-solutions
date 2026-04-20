# CS50P - Introduction to Programming with Python

## notes: Lecture 2 - Loops
+ original notes: [course site](https://cs50.harvard.edu/python/notes/2/)

### LOOP
+ used for repeated actions

### WHILE LOOP
+ while loop is executed while a condition is True
```python
while condition:
```
+ e.g.
```python
i = 0
while i < 3:
    print("meow")
    i += 1
```
+ in general, counting starts at 0 in programming
+ += operator: the value on right is added to the variable on the right, e.g. i += 1 is the same as i = i + 1
+ -= operator: the value on right is subtracted from the varuable on the right, e.g. i -= 1 is the same as i = i - 1
+  a common paradigm within python is to use a while loop to validate the input of the user
```python
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
```
+ while True: is a infinited loop
+ the keyword continue continues the loop
+ the keyword break stops the loop
+ instead of break, return can be used as well, then the loop is stopped and a value is returned
```python
def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
```

### FOR LOOP
+ for loop is executed for a defined numbers of executions or for iterating over a sequence (e.g. lists)
```python
for i in list:
```
+ e.g.
```python
for i in [0, 1, 2]:
    print("meow")
```

### RANGE FUNCTION
+ range() returns a sequence of numbers starting with 0 (default) with increments of 1 (default), e.g. 
```python
for i in range(3):
    print("meow")
```
+ the stop value is exclusive, that means the range() functions counts only to stop-1, e.g. the output for range(3) is 0,1,2
+ if a varibale has no significance in a code (e.g. only used ones) , a variable is represented by a underscore(_) -> it is more pythonic, e.g.
```python
for _ in range(3):
    print("meow")
```

### LIST
+ a list is a variable contaning mulitple values (**ITEMS**)
+ a list is represented by [], items are seperarted by , in a list
```python
numbers = [0,1,2,3,4,5]
```
+ the first item has the index 0, the second item has the index 1, and so on
+ the last item has the index -1, the second last item has the index -2. and so on
+ list slicing with the syntax list \[start : end : step]
+ start, end, and step are optional

| | description |
| --- | --- |
| list\[i] | returns the item with the index i |
| list\[i:j] | returns the items from index i (i is inclusive) to index j (j is exclusive) |
| list\[i:] | returns items from index i (i is inclusive) to the end of the list |
| list\[:i] | returns items from the start of the list to index i (i is exlusive);  same as list\[0:i] |
| list\[::-1] | returns reversed list |
+ e.g.
```python
numbers = [0,1,2,3,4,5]

numbers[2] #output: 2
numbers[1:3] #output: [1,2]
numbers[0:3] #output: [0,1,2]
numbers[:3] #output: [0,1,2]
numbers[2:] #output: [2,3,4,5]

numbers[-1] #output: 5
numbers[-3:-1] #output: [3,4]
numbers[-2:] #output: [4,5]
numbers[:-4] #output: [0,1]
```  
+ list methods

| methods | description |
| --- | --- |
| list.append() | adds an item to the end of the list |
| list.remove(i) | removes first occurence of the item i in the list |
| list.insert(i, j) | adds item j at index i in the list |
| list.reverse() | revereses all items in the list |
| list.pop() | removes and returns last item in the list |
| list.clear() | removes all items in the list |
+ list comprehensions without and with if condition
```python
[i for i in list]
[i for i in list if condition]
```
+ e.g.
```python
numbers = [0,1,2,3,4,5]

[number for number in numbers] #output: [0, 1, 2, 3, 4, 5]
[number for number in numbers if number < 3] #output: [0, 1, 2]
```

### LEN FUNCTION
+ len() returns length of items in an object (e.g. string, list)
```python
numbers = [0,1,2,3,4,5]

len(numbers) #output: 6
```

### DICT
+ dictionary/dict is a structured variable with keys and assigned values
+ a key and an assigned value is a item, they are seperated by :
+ dict is represented by {}, items are seperarted by , in a dict
```python
numbers = {"one": 1, "two": 2, "three": 3}
```
+ for nice coding every item gets a seperate line:
```python
numbers = {
    "one": 1,
    "two": 2,
    "three": 3
}
```
+ according to PEP 8, the last item ends with a comma as well (technically the last comma is not necessary):
```python
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
}
```
+ the value is returned by the key:
```python
numbers["one"] #output: 1 
```
+ a keyerror indicates the absence of key and assigned value
+ dict methods

| methods | description |
| --- | --- |
| dict.update({i: j}) | adds an item (key i and value j) to the end of the dict, same as dict[i] = j|
| dict.get(i,j) | returns the value of the key i in the dict, if the key i is not in the dict j is returned (default: None) |
| dict.keys() | returns all keys of the dict |
| dict.values() | returns all values of the dict |
| dict.pop() | removes and returns last item in the dict |
| dict.clear() | removes all items in the dict |
+ dict comprehensions analouge to list comprehensions
```python
{i: function(i) for i in list}
{i: function(i) for i in list if condition}
```
+ list and dict can be combined to structured data, e.g.
```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
``` 

### None
+ keyword None indicating the absence of a value

### STRING SLICING 
+ analouge to list slicing
```python
string = "python"

string[2] #output: t
string[1:3] #output: yt
string[0:3] #output: pyt
string[:3] #output: pyt
string[2:] #output: thon

string[-1] #output: n
string[-3:-1] #output: ho
string[-2:] #output: on
string[:-4] #output: py
``` 

### TUPLE
+ a tuple is an **immutable** variable contaning mulitple items 
+ a tuple is represented by (), items are seperarted by , in a tuple
+ tuples have a smaller size compared to lists -> higher performance
+ tuple can be unpacked, e.g.
```python
x,y = (i, j)

x #output: i
y #output: j
```

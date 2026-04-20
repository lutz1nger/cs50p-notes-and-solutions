# CS50P - Introduction to Programming with Python

## notes: Lecture 4 - Libraries
+ original notes: [course site](https://cs50.harvard.edu/python/notes/4/)

### LIBRARIES
+ collection/module with functions or features, which can be integrated into a code
+ always read the documentation of a library

### RANDOM
+ library/module to generate randomness containing e.g. following functions

| function | description |
| --- | --- |
| random.choice(seq) | returns a random value from seq |
| random.choices(seq, k = i) | returns i random values from seq without removing the returned value (default k = 0); shuffling with replacement |
| random.sample(seq, k = i) | returns i random values from seq with removing the returned value (default k = 0); shuffling without replacement |
| random.randint(i,j) | generates random integer between i and j |
| random.shuffle(list) | randomize a list in place |
| random.seed(i) | generates the seed i with always the same output; e.g. for debugging |

+ to load a library, the keyword import is used, e.g.
```python
import random
```
+ then all functions of the library are loaded
+ the built-in function can be called by \<library name>.function(), e.g.
```python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```
+ loading on a specific function in a library, the keywords from and import is used, e.g.
```python
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```
+ it can increase readabilty of a code; however, watch out for shadowing (occurs when a variable defined within a local scope (like a function) has the same name as a variable in an outer scope, making the outer variable inaccessible within that local context)

### STATISTICS
+ library/module for statistical calculations, e.g. for the calculation of a mean value
```python
import statistics

print(statistics.mean([100, 90]))
```

### COMMAND-LINE ARGUMENTS
+ arguments are inputed in the command line with the execution of the code
+ therefore, the library can be used, e.g.
```python
import sys

print("hello, my name is", sys.argv[1])
```
+ by entering "python name.py David" the programm is executed
+ sys.argv (argument vector) is a list within sys that stores command-line arguments passed to the program
+ the first element of sys.argv(sys.argv\[0]) is always the name of the programm
+ a to low or high amount of arguments results in a IndexError; therefore, the input must be checked for errors:
```python
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
```
+ in good coding practice, error checking is seperated from remainder, e.g.
```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
```
+ sys.exit(msg) returns the message msg and exits the programm
+ by slicing several arguments can be processed and the first argument (programm name) can be ignored, e.g.
```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
```

### PACKAGES
+ third-party libraries implemented as a folder
+ [PyPI](https://pypi.org/) (python package index) is a repository or directory of all available third-party packages currently available
+ packages can be installed by the package manager pip; therefore, pip install \<library> is entered in the terminal
+ then the package can be loaded by the keyword import, e.g. cowsay (program that generates ASCII art pictures of animals with a message)
```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
```

### API
+ application porgramming interface (API) is a set of rules and protocols that acts as an intermediary, allowing different software applications to communicate and exchange data with each other without needing to understand their underlying code
+ always read the documentation of an API
+ to access APIs through the internet like e.g. iTunes, the libraries requests is necessary
```python
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
```
+ requests.get() allows to make a request to a website
+ since the response is a JSON file, it must be converted into a python dictionary by response.json()
+ JSON file (javascript object notation) is a common format to store and transport data in a text file
+ generally, it is a dictionary, e.g.
```json
{
 "resultCount":1,
 "results": [
{"wrapperType":"track", "kind":"song", "artistId":115234, "collectionId":1440852447, "trackId":1440853193, "artistName":"Weezer", "collectionName":"Everything Will Be Alright In the End", "trackName":"Go Away", "collectionCensoredName":"Everything Will Be Alright In the End", "trackCensoredName":"Go Away", "artistViewUrl":"https://music.apple.com/us/artist/weezer/115234?uo=4", "collectionViewUrl":"https://music.apple.com/us/album/go-away/1440852447?i=1440853193&uo=4", "trackViewUrl":"https://music.apple.com/us/album/go-away/1440852447?i=1440853193&uo=4", 
"previewUrl":"https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/07/eb/37/07eb3790-05a1-37fa-7578-f69902bcd864/mzaf_11467306212093211989.plus.aac.p.m4a", "artworkUrl30":"https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/27/c3/64/27c36409-018a-48cb-d9b2-23212f58d123/14UMGIM36905.rgb.jpg/30x30bb.jpg", "artworkUrl60":"https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/27/c3/64/27c36409-018a-48cb-d9b2-23212f58d123/14UMGIM36905.rgb.jpg/60x60bb.jpg", "artworkUrl100":"https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/27/c3/64/27c36409-018a-48cb-d9b2-23212f58d123/14UMGIM36905.rgb.jpg/100x100bb.jpg", "collectionPrice":9.99, "trackPrice":1.29, "releaseDate":"2014-10-07T12:00:00Z", "collectionExplicitness":"notExplicit", "trackExplicitness":"notExplicit", "discCount":1, "discNumber":1, "trackCount":13, "trackNumber":8, "trackTimeMillis":193639, "country":"USA", "currency":"USD", "primaryGenreName":"Alternative", "isStreamable":true}]
}
```
+ to make the json readable for python, the library json with the function json.dumps() is necessary, e.g.
```python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
```
+ since JSON file are dictionaries, the values can be called , e.g.
```python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
```
+ the code can be optimized by the function response.raise_for_status() from the requests library (connection check; HTTP status code 200 means the connection is ok) and the error requests.HTTPError (connection failed), e.g.
```python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

try:
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
    response.raise_for_status()
except requests.HTTPError:
    print("Connection failed!")
   
o = response.json()
for result in o["results"]:
    print(result["trackName"])
```

### MAKING OWN LIBRARIES
+ a own library is just a python file with defined functions, e.g. here the python file sayings.py
```python
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")
```
+ to load the own libraries, the keyword import is used
```python
import sys

import sayings

if len(sys.argv) == 2:
    sayings.goodbye(sys.argv[1])

#or

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
```
+ to load a own libraries, the python files (library and program) must be in the same folder or the folder with the python file of the library must be registered in PYTHONPATH
+ for e.g. debugging, in the library a main function can be added, e.g.
```python
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()
```
+ description of if \_\_name\_\_ == "\_\_main\_\_": main():
    + every python file has a variable called \_\_name\_\_
    + if the python file is executed, \_\_name\_\_ is assigned as "\_\_main\_\_" (the main() is executed for e.g. debugging)
    + if the python file is imported as library in another python file, \_\_name\_\_ is assigned as \<python file name> (the main() is not executed)
    + e.g. the python file "file1.py" is executed, then  \_\_name\_\_ is "\_\_main\_\_"; the python file "file1.py" is imported in another python file, then  \_\_name\_\_ is "file1"

### MAKING OWN PACKAGE
+ a own package can be made by placing files in the folder
+ additionally, a file with the name "\_\_init\_\_.py" must be added in the folder
+ the folder must be in the same folder as the python file using the package or  must be registered in PYTHONPATH
+ e.g.
```
├── dir
│   ├── __init__.py
│   ├── file1.py
│   └── file2.py
└── file3.py
```
+ to load the packackage, the keyword import is used:
```python
import dir.file1
dir.file1.function1()

#or

from dir.file1 import function1
function1()
```

### CODING STYLE
+ a common style guide for python code is [PEP 8](https://peps.python.org/pep-0008/)
+ the highest priority of coding has the readability of a code, which can be achivied by consistency (e.g. indentation (in general, 4 spaces), blank lines, imports, ...)
+ following libraries can help to clean up the code regarding PEP 8 (all can be installed using pip):
    + [Pylint](https://pypi.org/project/pylint/)
    + [pycodestyle](https://pypi.org/project/pycodestyle/)
    + [black](https://pypi.org/project/black/) -> for exceution in the terminal: black \<python file name>.py

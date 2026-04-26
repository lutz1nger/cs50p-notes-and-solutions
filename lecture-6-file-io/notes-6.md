# CS50P - Introduction to Programming with Python

## notes: Lecture 6 - File I/O
+ original notes: [course site](https://cs50.harvard.edu/python/notes/6/)

### FILE I/O

sorted

open
-> input: name of file and how to open with "w" 
-> if file not available it creates file
-> w dangerous -> recreating
-> a append
    file.write do not a newline 

with
with in this context -> more phytonic
r -read mode 
readlines()
sorted(file)
sorted(, reverse=True)

csv
comma seperated values
unpack
dic -> single quotes on the inside

key 
python allows functions as parameter
lambda function

csv library
reader -> list
dictreader return dict csv in first line
writer -> list handels escpaing
dictwriter needs a cs with paramter

PIL
pillow -> image files

shorts:
good practice: Image opne and clsoe. or with
img.size
img.format
img.rotate(180)
form PIL import ImageFilter
img.filter(ImageFilter.BLUR)
img.filter(ImageFilter.FIND_EDGES)

for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
        isnstead
        for row in reader:
        students.append(row)
with can use two files open at once
fieldnames will be create
reader.fieldnames -> writer.writeheader()
add new dict to row[key]

file.read()
write
writelines




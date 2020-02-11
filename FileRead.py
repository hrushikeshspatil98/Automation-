""" File Handling:
To open file : open()
Modes of opening:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
Additional modes: 
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode
"""
#Open File
f=open("D:\\a.txt","r")
#Read contents in file
print(f.read())
#Close File
f.close()

"""Output
a
b
c
d
e
"""

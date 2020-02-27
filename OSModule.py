#The python OS module provides functions used for interacting with the operating system and also get related information about it.
#The python OS module lets us work with the files and directories.
import os

#This function provides the name of the operating system module that it imports.
#Currently, it registers 'posix', 'nt', 'os2', 'ce', 'java' and 'riscos'.
print(os.name)
print("Current Working Directory is:",os.getcwd()) #Displays Current Working Directory of the file

fd="D:\\Hrushi\\T\\a.txt"
# Checking path exits or not with os.F_OK   
path=os.access(fd,os.F_OK)   
print("Exist path:",path)   
# Checking read access with os.R_OK   
path=os.access(fd,os.R_OK)   
print("access to read the file:",path)       
# Checking write access with os.W_OK   
path=os.access(fd,os.W_OK)   
print("access to write the file:",path)       
# Checking execute access with os.X_OK   
path=os.access(fd,os.X_OK)   
print("access to exicute te path:",path)  

#a file or directory can be renamed by using os.rename() fn,if user has rights to change file
os.rename(fd,"D:\\Hrushi\\T\\b.txt")
print("File renamed from a.txt to b.txt") 

#a file or directory is removed by using remove() and rmdir() fn respectively.
os.remove("D:\\Hrushi\\T\\b.txt")
os.rmdir("D:\\Hrushi\\T\\a")

"""
Output:
nt
Current Working Directory is: C:\Users\Hrushi\.spyder-py3
Exist path: True
access to read the file: True
access to write the file: True
access to exicute te path: True
File renamed from a.txt to b.txt
"""

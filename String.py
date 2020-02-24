firstName="Hrushikesh"
lastName="patil "
name=firstName+" "+lastName
print("Name:",name)  #String Concatenation
print("Type:",type(name))
fname=firstName.lower()
lname=lastName.upper()
print("First character in name is:",firstName[0])
print("First Name in lower case:",fname) #Converts string to Lower case.
print("Last Name in upper case:",lname)    #Converts string to Upper case.
print("Is first name",fname," in lower case:",fname.islower())
print("Is last name ",lname,"in upper case:",lname.isupper())
print("Is name ",name,"contains digit:",name.isdigit())
print("Is name ",name,"is alphanumeric:",name.isalnum())
print("Is first name",fname,"ends with 'sh':",fname.endswith("sh"))
print("Is first name",fname,"starts with 'hru':",fname.endswith("sh"))
print("Is first name",fname,"contains only alphabets:",fname.isalpha())
print("First Name after swapcase case:",firstName.swapcase())  #Inverts all characters in string
print("After capitalizing:",name.capitalize())
print("Length of string is:",len(name))  #Length of string
print("Enter substring to find:")
fstr=input()
print("Substring ",fstr,"found at position:",name.find(fstr))
name="$"+name
print("Name: ",name)
#We can use direct strip() fn to remove all leading and trailing whitespaces or character specified
#name=name.strip()
name=name.lstrip("$ ")  #Removes all leading whitespaces or character specified in fun parm
name=name.rstrip()  #Removes all trailing whitespaces 
print("Name after removing whitespaces or char specified:",name)
print("Length of string is:",len(name))
name=name.replace("kesh","")
print("Name after Replacing:",name)
print("Length of string is:",len(name))
#Split string 
listStr=name.split()
print("After Split: ")
print(listStr)

"""Output:
Name: Hrushikesh patil 
Type: <class 'str'>
First character in name is: H
First Name in lower case: hrushikesh
Last Name in upper case: PATIL 
Is first name hrushikesh  in lower case: True
Is last name  PATIL  in upper case: True
Is name  Hrushikesh patil  contains digit: False
Is name  Hrushikesh patil  is alphanumeric: False
Is first name hrushikesh ends with 'sh': True
Is first name hrushikesh starts with 'hru': True
Is first name hrushikesh contains only alphabets: True
First Name after swapcase case: hRUSHIKESH
After capitalizing: Hrushikesh patil 
Length of string is: 17
Enter substring to find:
ush
Substring  ush found at position: 2
Name:  $Hrushikesh patil 
Name after removing whitespaces or char specified: Hrushikesh patil
Length of string is: 16
Name after Replacing: Hrushi patil
Length of string is: 12
After Split: 
['Hrushi', 'patil']
"""

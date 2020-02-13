#Dictionary 
dict_emp={ "Name":"Akshay","Company":"Google","Salary":25000} #Creating the dictionary
print("Type: ",type(dict_emp))
print("Length of dictionary is: ",len(dict_emp))
#print("Dictionary is: ",dict_emp)
print("All keys in dictionary are: ",dict_emp.keys())
print("All Values in dictionary are: ",dict_emp.values())
print("All Key Value Pairs in dictionary are: ",dict_emp.items())
print("Employee data->")
print("Name: %s" % dict_emp["Name"])
print("Company: %s" % dict_emp["Company"])
print("Salary: %d" % dict_emp.get("Salary"))
#Adding items
dict_emp["Age"]=23
print("After adding Dictionary is: ",dict_emp)
#Update dictionary element
dict_emp["Salary"]=30000
print("After Updating, Dictionary is: ",dict_emp)
#Delete element in dictionary
del dict_emp["Age"]
print("After Deleting, Element Dictionary is: ",dict_emp)
#print all the keys of a dictionary
for i in dict_emp:
    print(i)
#print all the values of a dictionary
for i in dict_emp:
    print(dict_emp[i])
#print the values of the dictionary by using values() method.
for i in dict_emp.values():
    print(i)
#print the key-value pairs of the dictionary by using items() method.
for i in dict_emp.items():
    print(i)
#print key-value pairs using one for loop
for i,j in dict_emp.items():
    print(i,": ",j)
#Check key exists in dictionary or not
if "Name" in dict_emp:
    print("Name is present in dict_emp")
dict_emp["Locn"]="Pune"
dict_emp.pop("Salary")  #removes the item with the specified key name
dict_emp.popitem()      #removes the last inserted item (after py 3.7v)
print("Dictionary is: ",dict_emp)
dict_emp.clear()
print("After Clearing, Dictionary is: ",dict_emp)

"""
Output:
Type:  <class 'dict'>
Length of dictionary is:  3
All keys in dictionary are:  dict_keys(['Name', 'Company', 'Salary'])
All Values in dictionary are:  dict_values(['Akshay', 'Google', 25000])
All Key Value Pairs in dictionary are:  dict_items([('Name', 'Akshay'), ('Company', 'Google'), ('Salary', 25000)])
Employee data->
Name: Akshay
Company: Google
Salary: 25000
After adding Dictionary is:  {'Name': 'Akshay', 'Company': 'Google', 'Salary': 25000, 'Age': 23}
After Updating, Dictionary is:  {'Name': 'Akshay', 'Company': 'Google', 'Salary': 30000, 'Age': 23}
After Deleting, Element Dictionary is:  {'Name': 'Akshay', 'Company': 'Google', 'Salary': 30000}
Name
Company
Salary
Akshay
Google
30000
Akshay
Google
30000
('Name', 'Akshay')
('Company', 'Google')
('Salary', 30000)
Name :  Akshay
Company :  Google
Salary :  30000
Name is present in dict_emp
Dictionary is:  {'Name': 'Akshay', 'Company': 'Google'}
After Clearing, Dictionary is:  {}
"""

#16 Lists
#List is a collection of elements which is ordered and changeable. Allows duplicate members.

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
num_list=[10,20,30]
#Join two lists
comb_list=thislist+num_list
print("Joined List:",comb_list)
thislist.extend(num_list)
print("thislist after extension:",thislist)

""" Output: 
Yes, 'apple' is in the fruits list
Joined List: ['apple', 'banana', 'cherry', 10, 20, 30]
thislist after extension: ['apple', 'banana', 'cherry', 10, 20, 30]
"""

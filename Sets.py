#Set
#A set is a collection which is unordered and unindexed. 
#In Python sets are written with curly brackets.

num_set={15,30,45,60,75,90}
print("Type: ",type(num_set))
print("Set: ",num_set)
if 45 in num_set:
    print("45 is in given set")
else:
    print("45 is not in given set")
#Add items in set
num_set.add(105)  #To add one item in set
num_set.update([120,135,150])  #To add more than one items in set
print("After adding items in set: ")
for i in num_set:
    print(i,end=' ')
#Remove items in set
num_set.pop() #It will remove last item in set,so we will not know which item gets removed because sets are unordered.
num_set.discard(15)  #If the item to remove does not exist, discard() will NOT raise an error.
#num_set.remove(15)  #If the item to remove does not exist, remove() will raise an error.
print("\nlength of set is: ",len(num_set))
print("Set: ",num_set)
num_set.clear()
print("Set after clear: ",num_set)
#Delete set
del num_set
print("Set deleted..")

"""
Output:
Type:  <class 'set'>
Set:  {75, 45, 15, 90, 60, 30}
45 is in given set
After adding items in set: 
135 105 75 45 15 150 120 90 60 30 
length of set is:  8
Set:  {105, 75, 45, 150, 120, 90, 60, 30}
Set after clear:  set()
Set deleted..
"""

#Frozenset 
frozenSet=frozenset([10,20,30,40,50])
print("Type of set: ",type(frozenSet))
print("Items in frozenSet are: ")
for i in frozenSet:
    print(i,end=" ")

#This gives an error 'frozenset' object has no attribute 'add' or 'remove' since we cannot change the content of Frozenset after creation   
#frozenSet.add(60)
#frozenSet.remove(50)

"""
Type of set:  <class 'frozenset'>
Items in frozenSet are: 
40 10 50 20 30 
"""

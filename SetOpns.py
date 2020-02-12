#Set Operations
set_col1={"Orange","Blue","White","Yellow","Black","Green","Violet"}
print("Set 1: ",set_col1)
set_col2=set(("Orange","Blue","Black"))
print("Set 2: ",set_col2)
#Union
print("set1 | set2:",set_col1 | set_col2) #opr. | used for Union
print("set1 | set2:",set_col1.union(set_col2)) #Using union() method
#Intersection  
print("set1 & set2:",set_col1 & set_col2) #opr. & used for Intersection
print("set1 & set2:",set_col1.intersection(set_col2)) #Using intersection() method
#Difference
print("set1 - set2: ",set_col1-set_col2) #opr. - used for Difference
print("set2 - set1: ",set_col2-set_col1) #Using difference() method
#difference_update() modifies this set by removing all the items that are also present in the specified sets
print("set: ",set_col1.difference_update(set_col2))
#symmetric difference
print("symmetric difference betn set1 and set2 is:",set_col1.symmetric_difference(set_col2))
#Set comparisons
print("set1 is the Superset of set2: ",set_col1>set_col2)
print("set1 is the Subset of set2:",set_col1<set_col2)
print("set1 is equivalent to set2:",set_col1==set_col2)

"""
Output:
Set 1:  {'Green', 'White', 'Violet', 'Orange', 'Blue', 'Black', 'Yellow'}
Set 2:  {'Orange', 'Black', 'Blue'}
set1 | set2: {'Green', 'Violet', 'White', 'Orange', 'Blue', 'Black', 'Yellow'}
set1 | set2: {'Green', 'Violet', 'White', 'Orange', 'Blue', 'Black', 'Yellow'}
set1 & set2: {'Orange', 'Black', 'Blue'}
set1 & set2: {'Orange', 'Black', 'Blue'}
set1 - set2:  {'Green', 'White', 'Violet', 'Yellow'}
set2 - set1:  set()
set:  None
symmetric difference betn set1 and set2 is: {'Green', 'White', 'Violet', 'Orange', 'Blue', 'Black', 'Yellow'}
set1 is the Superset of set2:  False
set1 is the Subset of set2: False
set1 is equivalent to set2: False
"""

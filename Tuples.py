num_tuple=(10,20,30,40,50)
print("Type: ",type(num_tuple))
print(num_tuple)

#Access Tuple Items
print("First element is: ",num_tuple[0])
print("Other elemnts except first and last are: ",num_tuple[1:len(num_tuple)-1]) #Range of Indexes
print("Last element is: ",num_tuple[-1])   #Negative Indexing

#Change tuple values: Tuples are unchangeable so we can convert the tuple into a list, change the list,
# and convert the list back into a tuple.Follow same for insert and remove itmes.
a=list(num_tuple)
a[4]=60
num_tuple=tuple(a)
for i in num_tuple:             #print tuple items using loop 
    print(i,end=' ')

#check 30 exists or not in tuple
if 30 in num_tuple:
    print("\nYes, 30 exists in num_tuple..")
    
#Insertion and Deletion of tuple item
a=list(num_tuple)
a.insert(4,50)
a.pop(len(a)-1)
num_tuple=tuple(a)
print("Tuple is: ",num_tuple)

#Create another tuple using constructor
alph_tuple=tuple(('a','b','c'))
print(alph_tuple)
#Join two tuples
comb_tuple=num_tuple+alph_tuple
print("After joining: ",comb_tuple)

#Tuple Methods
print("Item 10 ocurrs",num_tuple.count(10),"time")
print("Item a found at index: ",comb_tuple.index('a'))

"""Output:
Type:  <class 'tuple'>
(10, 20, 30, 40, 50)
First element is:  10
Other elemnts except first and last are:  (20, 30, 40)
Last element is:  50
10 20 30 40 60 
Yes, 30 exists in num_tuple..
Tuple is:  (10, 20, 30, 40, 50)
('a', 'b', 'c')
After joining:  (10, 20, 30, 40, 50, 'a', 'b', 'c')
Item 10 ocurrs 1 time
Item a found at index:  5
"""

#Generators
#Python Generators are the functions that return the traversal object and used to create iterators.
#It traverses the entire items at once.

def table(n):  
    for i in range(1,11):  
        yield n*i  
  
for i in table(10):  
    print(i,end="  ")  

print("\n")    
list = [1,2,3,4,5,6]  
  
z = (x**3 for x in list)  
  
for i in range(len(list)):
    print(list[i],"** 3: ",next(z))
    
'''Output:
10  20  30  40  50  60  70  80  90  100  

1 ** 3:  1
2 ** 3:  8
3 ** 3:  27
4 ** 3:  64
5 ** 3:  125
6 ** 3:  216
'''

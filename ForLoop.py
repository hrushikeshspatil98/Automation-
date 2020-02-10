#4 For loop 
#Linear Search
arr=[10,30,20,40,50]
key=40
for i in arr:
    if (i == key):
        print("Element",i,"Found at position: ",arr.index(i)+1)
        
"""
Output:
  Element 40 Found at position:  4  
"""

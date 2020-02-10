#15 Recursion : function calls itself

arr=[10,20,30,40,50,60,70,80,90]   #array should be sorted for binary search

def binarySearch(i,key,j):
    
    mid=int((i+j)/2)
    
    if (key == arr[mid]):
        print("Element found at position: ",mid+1)
        
    if (key < arr[mid]):
        binarySearch(i,key,mid-1)
        
    if (key > arr[mid]):
        binarySearch(mid+1,key,j)

print("Enter element to search: ")
key=int(input())
binarySearch(0,key,len(arr))



""" Output: 
Enter element to search: 

60
Element found at position:  6
"""

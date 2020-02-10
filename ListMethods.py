#9 Some Imp. List/Arrays methods

"""append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""

arr=[10,30,50,70,90,20,40,60,80,100]

print("Array is:",arr)
print("Array 0-5 is: ",arr[0:5])
print("Length of an array is: ",len(arr))       #Length of an array    
#finding index of specified value 
key=int(input("Enter key element: "))           #take input from user             
print("Element found at: ",arr.index(key)+1)
arr.reverse()                               #Reverse order of an array
print("After Reverse:",arr)
arr.sort()                                  #Sorting elements in an array
print("After Sorting:",arr)
#Insert element at last
arr.append(110)
print("After Inserting, Array is:",arr)
#Insert element at specified position
arr.insert(0,0)
print("After Inserting, Array is:",arr)
#Removes the element at the specified position
arr.pop(0)
print("After Deleting, Array is:",arr)
#Removes the first element with the specified value
arr.remove(110)
print("After Deleting, Array is:",arr)
#Removes all the elements from the list
arr.clear()
print("After Deleting All, Array is:",arr)

"""
Output:
Array is: [10, 30, 50, 70, 90, 20, 40, 60, 80, 100]
Array 0-5 is:  [10, 30, 50, 70, 90]
Length of an array is:  10

Enter key element: 70
Element found at:  4
After Reverse: [100, 80, 60, 40, 20, 90, 70, 50, 30, 10]
After Sorting: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
After Inserting, Array is: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
After Inserting, Array is: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
After Deleting, Array is: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
After Deleting, Array is: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
After Deleting All, Array is: []
"""

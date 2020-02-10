#8 Arrays: *No built in support for arrays in python, it uses lists.
#Bubble Sort
arr=[90,50,20,30,40,70,10,80,60,100]

for i in range(0, len(arr)):
    for j in range(0,len(arr)-1):
        if (arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print("Sorted Array is: ",arr)

"""
Output:
Sorted Array is:  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""

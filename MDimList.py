#Multidimensional Array\List
#Multiplication of two matrices
mList1=[[1,2,3],[4,5,6],[7,8,9]]
mList2=[[1,2,3],[4,5,6],[7,8,9]]
mList3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,len(mList1)):
    
    for j in range (0,len(mList2[0])):
        sum=0
        for k in range (0,len(mList2)):
            sum=sum+ mList1[i][k]* mList2[k][j]
        mList3[i][j]=sum
print("After Multiplication: ")
for i in mList3:
    print(i)
    
"""
Output:
After Multiplication: 
[30, 36, 42]
[66, 81, 96]
[102, 126, 150]
"""

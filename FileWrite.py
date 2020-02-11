#Open File in write mode
f=open("D:\\a.txt","w")
f.write("10\n20\n30")  #Write contents in file
f.close()  #close the file
#Open File in read mode
f=open("D:\\a.txt","r")
print("Data in file: ")
print(f.read())
f.close()

"""Output
Data in file: 
10
20
30
"""

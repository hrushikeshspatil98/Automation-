#Open File in read and binary mode
fin=open("D:\\a.png","rb")
x=fin.read()

#Open File in write and binary mode
fout=open("D:\\b.png","wb")
fout.write(x)
print("File Copied Successfully..")

fin.close()
fout.close()

"""Output
File Copied Successfully..
"""

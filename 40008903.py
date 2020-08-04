
import os

with open("D:\input.txt","r") as file1,open("D:\output.txt","a") as file2:
         
         for i in file1:
             inp=file1.readline()
             name,s1,s2,s3 = inp.split(',')
             total=int(s1)+int(s2)+int(s3)
             res=name+","+str(s1)+","+str(s2)+","+str(s3)+","+str(total)
             file2.write(str(res))
             
print("End")
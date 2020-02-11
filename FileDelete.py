import os
#Check file or folder exists or not
if os.path.exists("D:\\a.png" and "D:\\dirPY"):
    os.remove("D:\\a.png")
    os.rmdir("D:\\dirPY")  #Delete folder only if folder is empty
    
    print("File a.png and folder dirPY deleted Successfully..")
else:
    print("The file does not exist")

"""
Output:
File a.png and folder dirPY deleted Successfully..
"""

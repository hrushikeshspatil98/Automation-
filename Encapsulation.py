#12 Classes and Objects , Encapsulation

class Employee:
    eID=0
    eName=""
    eADD=""
    count=0
    
    def __init__(self, eID, eName):
        self.eID=eID
        self.eName=eName
        Employee.count=Employee.count+1
    
    def displayData(self):
        print("Employee ID: ",self.eID)
        print("Employee Name: ",self.eName)
    

e= Employee(66115,"Hrushikesh Patil")
e.displayData()
e.eID=661153
e.displayData()

#Delete Object Properties
del e.eName
print("No of employees are: ",e.count)
#Delete Object
del e
print("Object deleted")
# print("No of employees are: ",e.count)  #It will gives error e is not defined..

""" Output: 
Employee ID:  66115
Employee Name:  Hrushikesh Patil
Employee ID:  661153
Employee Name:  Hrushikesh Patil
No of employees are:  1
Object deleted    
"""

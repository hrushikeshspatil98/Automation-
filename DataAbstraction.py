#13 Data abstraction
#In python, we can also perform data hiding by adding the double underscore (___) as a prefix to the attribute which is to be hidden.

class Employee:
    eID=0
    eName=""
    eADD=""
    __count=0
    
    def __init__(self, eID, eName):
        self.eID=eID
        self.eName=eName
        Employee.__count=Employee.__count+1
    
    def displayData(self):
        print("Employee ID: ",self.eID)
        print("Employee Name: ",self.eName)
    
try: 
    e= Employee(19,"Hrushikesh Patil")
    e.displayData()
    print("No of employees are: ",e.__count)

except:
    print("var count is not accessible..")

""" Output: 
Employee ID:  19
Employee Name:  Hrushikesh Patil
var count is not accessible.. 
"""

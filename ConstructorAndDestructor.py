#Constructor and Destructor 
class Employee:
    
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print('In Constructor: \nEmployee created.')
        
    def __del__(self):
        print('In Destructor:  \nEmployee deleted.') 
    
    def displayInfo(self):
        print("Employee ID: ",self.id)
        print("Employee Name: ",self.name)
        
        
emp=Employee(101,"A B C")
emp.displayInfo()
del emp
        
""" Output:
In Constructor: 
Employee created.
Employee ID:  101
Employee Name:  A B C
In Destructor:  
Employee deleted.
"""



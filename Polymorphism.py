class Red(): 
     def ex(self): 
       print("Red color fruit: Apple") 
     def color(self):
       print("Red") 
class Orange(): 
     def ex(self): 
       print("Orange color fruit: Orange") 
     def color(self): 
       print("Orange") 
      
def func(obj): 
       obj.ex() 
       obj.color()
        
obj_red = Red() 
obj_orange = Orange() 
func(obj_red) 
func(obj_orange)

"""
Output:
Red color fruit: Apple
Red
Orange color fruit: Orange
Orange
"""

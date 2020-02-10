#Multiple Inheritance
class Addition:
    
    def add(self,a,b):
        print("Addition of ",a,"+",b,"is: ",a+b)

class Subtraction:
    
    def sub(self,a,b):
        print("Addition of ",a,"-",b,"is: ",a-b)

class Multiplication:
    
    def mult(self,a,b):
        print("Multiplication of ",a,"*",b,"is: ",a*b)

class Division:
    
    def div(self,a,b):
        print("Division of ",a,"/",b,"is: ",a/b)

class Calculate(Addition,Subtraction,Multiplication,Division):
    pass

c=Calculate()
c.add(40,25)
c.sub(45,20)
c.mult(12,13)
c.div(40,20)

print(issubclass(Calculate,Addition))  #Returns true is Calculate is subclass of Addition
print(isinstance(c,Calculate))         #Returns true is c is instance of Calculate

""" Output: 
Addition of  40 + 25 is:  65
Addition of  45 - 20 is:  25
Multiplication of  12 * 13 is:  156
Division of  40 / 20 is:  2.0
True
True
"""

#Method Overriding

class A:
    
    def swap(self,a,b):
        temp=a
        a=b 
        b=temp
        print("In A")
        print(a," ",b)

class B(A):
    
    def swap(self,a,b):
       a=a+b 
       b=a-b
       a=a-b
       print("In B")
       print(a," ",b)
       
b= B()    
b.swap(10,20)   #swap() of class B because object is of class B


""" Output: 
In B
20   10
"""

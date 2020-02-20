#Creating Thread Using Threading Module
"""
To implement a new thread using the threading module, you have to do the following −
-Define a new subclass of the Thread class.
-Override the __init__(self [,args]) method to add additional arguments.
-Then, override the run(self [,args]) method to implement what the thread should do when started.
Once you have created the new Thread subclass, you can create an instance of it and then start a new thread 
by invoking the start(), which in turn calls run() method. """

import threading 

class MyThread(threading.Thread):
 
        
    def __init__(self,flag):
        self.flag=flag
        threading.Thread.__init__(self)
      
    def run(self):
        if (self.flag==1):
            self.fx1()
        elif (self.flag==2):
            self.fx2()
   
    def fx1(self):
        for i in range(0,100):
            print("A",end="")
    
    def fx2(self):
        for i in range(0,100):
            print("B",end="")

mt1=MyThread(1)
mt1.start()
mt2=MyThread(2)
mt2.start()

for i in range(0,100):
            print("C",end="")
            
""" Output:
ABAAAAAACBBAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBACCCCBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBCAAAAAAAAAAAAAAAAAAAAAAAAA
AAAABCCCCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAA
AAAAAACCCCCCCCCCCCCCCCCCC
"""

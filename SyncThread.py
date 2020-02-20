#Synchronizing Threads

import threading 

threadLock=threading.Lock()
class MyThread(threading.Thread):
 
    def __init__(self,flag):
        self.flag=flag
        threading.Thread.__init__(self)
   
    def run(self):
        threadLock.acquire()  #Get lock to synchronize thread
        if (self.flag==1):
            self.fx1()
        elif (self.flag==2):  
            self.fx2()
        threadLock.release()  #Free lock to release next thread
        
    def fx1(self):
        for i in range(0,100):
            print("A",end="")
        print ("Exiting A Thread")
    
    def fx2(self):
        for i in range(0,100):
            print("B",end="")
        print ("Exiting B Thread")
            
threadList=[]
#Create new threads
mt1=MyThread(1)
mt2=MyThread(2)
#Adding threads in list
threadList.append(mt1)
threadList.append(mt2)
#Start Threads
mt1.start()
mt2.start()

for t in threadList:
    t.join() #join() waits for threads to terminate and after terminating resumes main thread

for i in range(0,50):
            print("C",end="")
print ("Exiting Main Thread")
 
            
""" Output:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAExiting A Thread
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBExiting B Thread
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCExiting Main Thread
"""

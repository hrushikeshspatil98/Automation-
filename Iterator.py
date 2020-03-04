class Even:
    
    def __init__(self, limit): 
        self.limit = limit
    
    def __iter__(self): 
        self.x = 2
        return self
    
    def __next__(self): 
  
        # Store current value of x 
        x = self.x 
  
        # Stop iteration if limit is reached 
        if x > self.limit: 
            raise StopIteration 
  
        # Else increment and return old value 
        self.x = x + 2; 
        return x 

# Prints even numbers from 2 to 20
for i in Even(20): 
    print(i,end=" ")
    
'''
class Even:
   
    def __iter__(self): 
        self.a = 2
        return self
    
    def __next__(self): 
        if self.a <= 20:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration

# Prints even numbers from 2 to 20
ev=Even()
myIter=iter(ev)
for i in myIter: 
    print(i,end=" ")
'''

'''Output:
2 4 6 8 10 12 14 16 18 20 
'''

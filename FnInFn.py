#Function inside Function

def factOfNum():
   
    num=0   #Not accessible in inside fn below
    def getInp():
        print("Enter a number: ")
        num=int(input())
        print("Number is: ",num)
        return num
    
    num=getInp()
    
    res=1
    for i in range (2,num+1):
        res=res*i
        
    print("Factorial of ",num,"is: ",res)
    
factOfNum()

"""
Output:
Enter a number: 
5
Number is:  5
Factorial of  5 is:  120
"""

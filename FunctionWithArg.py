#7 Function with Arguments:
num=17
def primeOrNot(n):
    i=2
    while (i <= n/2):
        if(n%i==0):
            return -1;
        i=i+1
    return 1;            

res=primeOrNot(num)
if (res==1):
    print(num,"is prime")
else:
    print(num,"is not prime")

"""
Output:
17 is prime
"""

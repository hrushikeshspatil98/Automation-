#Lambda Functions
#A lambda function is a function that can take any number of arguments, but can only have one expression.
#Syntax  lambda arguments : expression

x= lambda a:a*a*a

print(x(8))

def funSquare(x):
    return lambda num:num*x

x=int(input("Enter Number: "))
f=funSquare(x)

for i in range(1,11):
    print(x,"x",i,":",f(i))
    

"""
Output:
512

Enter Number: 15
15 x 1 : 15
15 x 2 : 30
15 x 3 : 45
15 x 4 : 60
15 x 5 : 75
15 x 6 : 90
15 x 7 : 105
15 x 8 : 120
15 x 9 : 135
15 x 10 : 150
"""

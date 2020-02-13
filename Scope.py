#Scope
a=10  #global scope

def fn1():
    b=20  #Local scope
    global c
    c=30
    print("A: ",a)
    print("A -> global scope")
    print("B: ",b)
    print("B -> local scope")

fn1()
print("C: ",c)
print("C -> global scope (using global keyword) ")

"""
A:  10
A -> global scope
B:  20
B -> local scope
C:  30
C -> global scope (using global keyword) 
"""

#Operators in python
#Arithmetic Operators: +,-,*,/,%,**(exponent/power),//(floor division)
a=15
b=3
print(a,"**",b,"= ",a**b)
b=3.5
print(a,"//",b,"= ",a//b)
#Comparison Operators: ==,!=,<,<=,>,>=,<>(same as !=)
b=3
print(a,">=",b,"= ",a>=b)
print(a,"!=",b,"= ",a!=b)
#Assignment Operators: =,+=,-=,*=,/=,%=,**=,//=
a /= b
a=int(a)
print("value of a is:",a)
#Bitwise Operators: &(AND),|(OR),^(XOR),~(Ones Complement),<<(Left Shift),>>(Right Shift)
print(a,"&",b,"= ",a&b)
print("~",a,"= ",~a)
print(a,">> 2 = ",a>>2)
#Logical Operators: and, or, not
if (a>3 and b>2):
    print(a,"> 3 and",b,"> 2")
#Membership Operators: in , not in
ls=[1, 2, 3, 4, 5 ]
print("List: ",ls)
if a in ls:
    print(a,"is available in the given list")
if 10 not in ls:
    print("10 is not available in the given list")   
#Identity Operators: is, is not
if a is b:
    print(a," and",b,"have same identity")
else:
    print(a," and",b,"do not have same identity")
b=a
print("After b=a")
if a is not  b:
    print(a," and",b,"do not have same identity")
else:
    print(a," and",b,"have same identity")

'''Output:
15 ** 3 =  3375
15 // 3.5 =  4.0
15 >= 3 =  True
15 != 3 =  True
value of a is: 5
5 & 3 =  1
~ 5 =  -6
5 >> 2 =  1
5 > 3 and 3 > 2
List:  [1, 2, 3, 4, 5]
5 is available in the given list
10 is not available in the given list
5  and 3 do not have same identity
After b=a
5  and 5 have same identity
'''

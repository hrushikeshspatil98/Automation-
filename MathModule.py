#Python math module includes trigonometric functions,representation functions,logarithmic functions,etc.
import math

num=16
print("GCD of 10 and 15 is:",math.gcd(10,15)) #GCD of two numbers
print("Factorial of 16 is:",math.factorial(num)) #Factorial of a number
print("Square root of",num," is:",math.sqrt(num)) #Square root of a number
print("4 to power 5 is:",math.pow(4,5))

#Logarithmic funs
print("log(",num,") to the base 2 is:",math.log(num,2))
print("log(",num,") to the base 10 is:",math.log10(num)) #
print("e^x (e^15): ",math.exp(num)) #Returns the value of E^x (e=2.718281 approximately)

#Trigonometric functions
degree=45
angleInRad=math.radians(degree) #Convert degrees to radians.
print("Sin(",int(math.degrees(angleInRad)),") is:",math.sin(angleInRad)) #Convert radians to degrees and return sine of 45 
print("Cos(",degree,") is:",math.cos(angleInRad)) # return cosine of 45 
print("Tan(",degree,") is:",math.tan(angleInRad)) # return tangent of 45 

"""Output:
GCD of 10 and 15 is: 5
Factorial of 16 is: 20922789888000
Square root of 16  is: 4.0
4 to power 5 is: 1024.0
log( 16 ) to the base 2 is: 4.0
log( 16 ) to the base 10 is: 1.2041199826559248
E^x (e^num):  8886110.520507872
Sin( 45 ) is: 0.7071067811865476
Cos( 45 ) is: 0.7071067811865476
Tan( 45 ) is: 0.9999999999999999
"""

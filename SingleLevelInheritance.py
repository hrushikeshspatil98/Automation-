#Single level inheritance

class Car:
    
    def displayVehicleType(self):
        print("Car <-")
    
class Maruti(Car):
    
    def displayBrand(self):
        print("Maruti")

m=Maruti()
m.displayVehicleType()
m.displayBrand()

""" Output: 
Car <-
Maruti
"""

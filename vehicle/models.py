from django.db import models

#Part 1: Base Model
class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    #Method
    def vehicle_info(self):
        return f"{self.brand} costs ${self.price:g}"
    
#Part 2: The Child Models
class Car(Vehicle):
    doors = models.IntegerField()

    def vehicle_info(self):
        # Method Overriding:
        return f"{self.brand} Car with {self.doors} doors costs ${self.price:g}"
    
class Motorcycle(Vehicle):
    helmet_included = models.BooleanField()

    def vehicle_info(self):
        # Method Overriding:
        return f"{self.brand} Motorcycle costs {self.price:g}"

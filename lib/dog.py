#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name="Pooch", breed="Mastiff"):
        if (type(name)== str) and (1 <= len(name) <= 25):
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")
        
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")
        

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if (type(name)== str) and (1 <= len(name) <= 25):
            self._name = name
            print(self._name)
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        print("Retrieving breed.")
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")



    pass

fido = Dog("Fido")
fido.set_name("")
print(fido.name)
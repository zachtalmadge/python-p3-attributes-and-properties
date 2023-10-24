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

    def __init__(self, name="tank", breed="bulldog"):
        self.name = name
        self.breed = breed
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        if len(name) < 1 or len(name) > 25:
            print('Name must be string between 1 and 25 characters.')
            return
        else:
            self.name = name

    name = property(get_name, set_name)
    
    def get_breed(self):
        return self.breed
    
    def set_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return
        else:
            self.breed = breed

    breed = property(get_breed, set_breed)

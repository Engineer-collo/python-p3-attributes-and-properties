class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="Buddy", breed="Beagle"):
        
        self.name = name  # Calls the setter
        self.breed = breed  # Calls the setter

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):

        return self._breed

    def set_breed(self, breed):
        if breed in self.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    # Define properties
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

dog1 = Dog()  
print(dog1.name)  # Retrieves "Buddy"
print(dog1.breed)  # Retrieves "Beagle"

dog1.name = "Max"  # Valid
dog1.breed = "Pug"  # Valid

dog1.name = ""  # Invalid, prints: "Name must be string between 1 and 25 characters."
dog1.breed = "Golden Retriever"  # Invalid, prints: "Breed must be in list of approved breeds."

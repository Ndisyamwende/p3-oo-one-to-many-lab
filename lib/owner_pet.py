class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []


    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet_type: {pet_type}. Allowed types are: {', '.join(self.PET_TYPES)}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all_pets.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all_types if pet.owner == self]


    def add_pets(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError("Invalid pet. Must be an instance of the Pet class.")

        pet.owner = self

    def get_sorted_pets(self):
        if not all(isinstance(pet, Pet) for pet in Pet.all_pets):
            raise ValueError("Invalid pets. All items must be instances of the Pet class.")

        return sorted(Pet.all_pets, key=lambda pet: pet.name)
    
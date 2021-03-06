from animal import Animal
from cat import Cat
from dog import Dog

class Home:
    def __init__(self,pets=[]):
        self.pets = pets

    def adopt_pet(self,pet):
        for each_pet in self.pets:
            if each_pet == pet:
                raise Exception ("You cant adopt twice")

        self.pets.append(pet)

    def sounds(self):
        return dog1.eat()    

if __name__== "__main__":
    home = Home()
    dog1 = Dog(" ","Barks")
    cat2 = Cat(" ","meows")

    home.adopt_pet(dog1)
    home.adopt_pet(cat2)

    print("The pets you can adopt")
    print(home.pets[0].eat)
    print(home.pets[1].eat)            

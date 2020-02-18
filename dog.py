from animal import Animal

class Dog(Animal):
    def __init__(self,eats,sounds):
        super().__init__(eats,sounds)

    def eat(self):
        return self.eats + "Food"

    def sounds(self):
        return self.sound,"Barks"

dog_1 = Dog(" ","Dog")
dog_1.eat()
#dog_1.sounds()

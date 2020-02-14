from animal import Animal

class Dog(Animal):
    def __init__(self,petname,sounds):
        super().__init__(petname,sounds)

    def food(self):
        print(self.name + " eats")

    def sounds(self):
        print(self.sound,"meows")

dog_1 = Dog("Rax","Dog")
dog_1.food()
dog_1.sounds()

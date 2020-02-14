from animal import Animal

class Cat(Animal):

    def __init__(self,petname,sound):
        super().__init__(petname,sound)

    def food(self):
        print(self.name + "eats")

    def sounds(self):
        print(self.sound,"meows")

cat_1 =Cat("stormy","cat")
cat_1.food()
cat_1.sounds()

from animal import Animal

class Cat(Animal):

    def __init__(self,eats,sound):
        super().__init__(eats,sound)

    # def eat(self):
    #     return(self.eats + "Food")

    # def sounds(self):
    #     return(self.sound)

cat_1 =Cat("Food ","Meow")
cat_1.eat()
print(cat_1.sounds())

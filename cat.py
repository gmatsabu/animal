from animal import Animal

class Cat(Animal):

    def __init__(self,eats,sound):
        super().__init__(eats,sound)

    def eat(self):
        return(self.eats + "Food")

    def sounds(self):
        return(self.sound,"Meow")

cat_1 =Cat(" ","cat")
cat_1.eat()
#cat_1.sounds()

class Animal:
    def __init__(self,petname,sound):
    
        self.name = petname 
        self.sound = sound


    def food(self):
        print("{} eats".format(self.name))

    def sounds(self):
        print("{} barks".format(self.sound))


dog = Animal("Rax","Dog")
cat = Animal("Stomy","Cat")

dog.food()
dog.sounds()

class Animal:
    def __init__(self,eats,sound):
    
        self.eats = eats 
        self.sound = sound

     
    def eat(self):
        return '{} Food'.format(self.eats)

    def sounds(self):
        return '{} Barks'.format(self.sound)


dog = Animal(" ","Dog")
cat = Animal(" ","Cat")

print (dog.eat())
print(cat.eat())
#dog.sounds()

class Animal:
    def __init__(self,eats,sound):
    
        self.eats = eats 
        self.sound = sound

     
    def eat(self):
        return self.eats
        #return '{} Food'.format(self.eats)

    def sounds(self):
        return self.sound
        #return '{} Barks'.format(self.sound)


dog = Animal("Food ","Barks")
cat = Animal("Food","Meow ")

print (dog.eat())
print(dog.sounds())
#dog.sounds()

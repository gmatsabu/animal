import unittest
from animal import Animal
from animal import Animal
class TestAnimal(unittest.TestCase):

      
    def setUp(self):
        print('setUp')
        self.cat1 = Animal('Food','Meow')
        self.dog1 = Animal('Food','Bark')  
    
    def test_eat(self):
        print('test_eats')
        self.assertEqual(self.cat1.eats,'Food')  
        self.assertEqual(self.dog1.eats,'Food')  

    def test_sound(self):
        print('test_sound')
        self.assertEqual(self.cat1.sound,'Meow')
        self.assertEqual(self.dog1.sound,'Bark')



if __name__ == '__main__':
    unittest.main()   
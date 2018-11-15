#AbstractFactory.py
class Dog:
    '''A simple dog class '''
    '''def __init__(self,name):
        self._name = name '''
    def speak(self):
        return 'Woof!'

    def __str__(self):
        return 'Dog'
class Cat:
    '''A simple dog class '''
    '''def __init__(self,name):
        self._name = name '''
    def speak(self):
        return 'Meow!'

    def __str__(self):
        return 'Cat'


class DogFactory:
    '''Concrete Factory'''
    
    def get_pet(self):
        """Return a Dog Object"""
        return Dog()
    
    def get_food(self):
        '''Return a dog food object'''
        return "Dog Chow"
    
class CatFactory:
    '''Concrete Factory'''
    
    def get_pet(self):
        """Return a Dog Object"""
        return Cat()
    
    def get_food(self):
        '''Return a dog food object'''
        return "Whiskas"

class PetStore:
    """PetStore house our Abstract Factory"""
    def __init__(self, pet_factory = None ):
        """petfactory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the obects returned by the tFactory """
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'".format(pet))
        print("Our pet say hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))

    def set_factory(self, pet_factory):
        self._pet_factory = pet_factory

#Create a concrete Factory
dog_factory = DogFactory()
#Create a pet store housing our abstract factory
shop = PetStore(dog_factory)
shop.show_pet()
#S

cat_factory = CatFactory()
#Create a pet store housing our abstract factory
shop = PetStore(cat_factory)
shop.show_pet()
#S


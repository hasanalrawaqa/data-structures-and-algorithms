from queue import Queue

class Animal:
    def __init__(self, species, name):
        """
        Represents an animal with a species and a name.

        Args:
            species (str): The species of the animal ("cat" or "dog").
            name (str): The name of the animal.
        """
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        """
        Represents an animal shelter that operates on a first-in, first-out basis.
        """
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        """
        Adds an animal to the shelter's queue.

        Args:
            animal (Animal): The animal to be added to the shelter.

        Raises:
            ValueError: If the animal species is neither "cat" nor "dog".
        """
        if animal.species == "dog":
            self.dog_queue.enqueue(animal)
        elif animal.species == "cat":
            self.cat_queue.enqueue(animal)
        else:
            raise ValueError("Animal species must be either 'cat' or 'dog'.")
        
    def dequeue(self, pref):
        """
        Removes and returns the oldest animal of the specified preference from the shelter's queue.

        Args:
            pref (str): The preference for either a "dog" or a "cat".

        Returns:
            Animal or None: The oldest animal of the specified preference, or None if the preference is invalid
                           or there are no animals of that preference in the queue.
        """
        if pref == "dog":
            if self.dog_queue:
                return self.dog_queue.dequeue(0)
        elif pref == "cat":
            if self.cat_queue:
                return self.cat_queue.dequeue(0)

        return None


if __name__ == '__main__':
    shelter = AnimalShelter()

# Enqueue some animals
shelter.enqueue(Animal("dog", "Buddy"))
shelter.enqueue(Animal("cat", "Whiskers"))
shelter.enqueue(Animal("dog", "Max"))
shelter.enqueue(Animal("cat", "Luna"))
# Dequeue a dog
dog = shelter.dequeue("dog")
print(dog.species, dog.name)  # Output: dog Buddy

# Dequeue a cat
cat = shelter.dequeue("cat")
print(cat.species, cat.name)  # Output: cat Whiskers

# Dequeue a non-existent animal
dog = shelter.dequeue("dog")
print(dog.species, dog.name)  # Output: dog Max

cat = shelter.dequeue("cat")
print(cat.species, cat.name) # Output: cat Luna
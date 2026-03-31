class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def __str__(self):
        return f"{self.name}, {self.age} years old, species: {self.species}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"

    def sleep(self):
        return f"{self.name} sleeps in its dog bed."


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color

    def speak(self):
        return f"{self.name} says: Meow!"

    def eat(self):
        return f"{self.name} nibbles on its food."
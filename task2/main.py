from models import Dog, Cat
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "Bulldog")
cat1 = Cat("Whiskers", 2, "White")
cat2 = Cat("Luna", 1, "Black")

animals = [dog1, dog2, cat1, cat2]

for animal in animals:
    print(animal)          
    print(animal.eat())    
    print(animal.sleep())  
    if hasattr(animal, 'speak'):
        print(animal.speak())  
    print("---")
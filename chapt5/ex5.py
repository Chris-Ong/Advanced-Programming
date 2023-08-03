class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        self.type = animal_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise

    def sayHello(self):
        print(f"{self.name} says hello!")

    def makeNoise(self):
        print(f"{self.name} makes a {self.noise} sound.")

    def animalDetails(self):
        print(f"Type: {self.type}")
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Noise: {self.noise}")

def main():
    dog = Animal("Dog", "Buddy", "Brown", 5, 15, "Bark")
    cow = Animal("Cow", "Daisy", "Black and White", 3, 500, "Moo")

    dog.sayHello()
    dog.makeNoise()
    dog.animalDetails()

    print("\n")

    cow.sayHello()
    cow.makeNoise()
    cow.animalDetails()

if __name__ == "__main__":
    main()

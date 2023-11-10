class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50

    def feed(self):
        self.happiness += 10
        print(f"{self.name} їсть і щасливий!")

    def play(self):
        self.happiness += 20
        print(f"{self.name} грається і щасливий!")


my_pet = Pet("Барсік", "Кіт")
print(f"Моя тварина: {my_pet.name}, Вид: {my_pet.species}")

my_pet.feed()
my_pet.play()

print(f"{my_pet.name} щастливість: {my_pet.happiness}")
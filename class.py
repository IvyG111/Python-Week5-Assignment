# Assignment 1: Design Your Own Class

# Step 1: Create a class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def show_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Price: ${self.price}"

    def upgrade_storage(self, additional_storage):
        self.storage += additional_storage
        return f"Storage upgraded. New storage: {self.storage}GB"

# Step 2: Add an inheritance layer to explore polymorphism or encapsulation
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, price, gpu):
        super().__init__(brand, model, storage, price)
        self.gpu = gpu

    def show_specs(self):
        base_specs = super().show_specs()
        return f"{base_specs}, GPU: {self.gpu}"

    def play_game(self, game):
        return f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU."

# Test the Smartphone class
phone = Smartphone("Samsung", "Galaxy S23", 128, 999)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 256, 1499, "Adreno 730")

print(phone.show_specs())
print(phone.upgrade_storage(128))
print(gaming_phone.show_specs())
print(gaming_phone.play_game("Genshin Impact"))
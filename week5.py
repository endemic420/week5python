class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.color = color

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def info(self):
        return f"{self.brand} {self.model}, {self.storage}GB, Color: {self.color}"


# Derived class: GamingSmartphone inherits from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, color, gpu, cooling_system):
        super().__init__(brand, model, storage, color)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        return f"Launching {game_name} on {self.brand} {self.model} with {self.gpu} GPU..."

    # Polymorphism - override info method
    def info(self):
        return f"{super().info()}, GPU: {self.gpu}, Cooling: {self.cooling_system}"


# Demo function to show class usage
def run_demo():
    phone1 = Smartphone("Apple", "iPhone 14", 128, "Midnight")
    phone2 = GamingSmartphone("Asus", "ROG Phone 6", 512, "Black", "Adreno 730", "Active Cooling")

    print("Basic Smartphone:")
    print(phone1.info())
    print(phone1.call("123-456-7890"))
    print()

    print("Gaming Smartphone:")
    print(phone2.info())
    print(phone2.call("098-765-4321"))
    print(phone2.play_game("Cyberpunk 2077"))


# Run the demo
if __name__ == "__main__":
    run_demo()

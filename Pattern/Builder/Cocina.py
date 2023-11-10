from PizzaBuilder import PizzaBuilder
from HawaiPizzaBuilder import HawaiPizzaBuilder
from BolognesePizzaBuilder import BolognesePizzaBuilder

## Lugar donode se crean pizzas y se envia la implementacion de builder

class Cocina:
    def set_pizza_builder(self, pb):
        self.pizza_builder = pb

    def get_pizza(self):
        return self.pizza_builder.get_pizza()

    def construir_pizza(self):
        self.pizza_builder.build_masa()
        self.pizza_builder.build_salsa()
        self.pizza_builder.build_relleno()


if __name__ == "__main__":
    cocinaBolognese = Cocina()
    bolognese_pizza_builder = BolognesePizzaBuilder()
    cocinaBolognese.set_pizza_builder(bolognese_pizza_builder)
    cocinaBolognese.construir_pizza()
    pizzaBolognese= cocinaBolognese.get_pizza()
    
    
    cocinaHawai = Cocina()
    hawai_pizza_builder = HawaiPizzaBuilder()
    cocinaHawai.set_pizza_builder(hawai_pizza_builder)
    cocinaHawai.construir_pizza()
    pizzaHawai = cocinaHawai.get_pizza()


    
    print(f"Pizza Hawaiana \n{pizzaHawai}\n")
    print(f"Pizza Bolognese \n{pizzaBolognese}")

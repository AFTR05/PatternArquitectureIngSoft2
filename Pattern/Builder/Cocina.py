from .PizzaBuilder import *

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
    cocina = Cocina()
    hawai_pizza_builder = HawaiPizzaBuilder()

    cocina.set_pizza_builder(hawai_pizza_builder)
    cocina.construir_pizza()

    pizza = cocina.get_pizza()
    print(pizza)
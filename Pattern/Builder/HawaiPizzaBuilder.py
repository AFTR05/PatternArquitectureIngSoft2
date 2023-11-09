
from PizzaBuilder import PizzaBuilder
from Pizza import Pizza

class HawaiPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza=Pizza()    

    def build_masa(self):
        self.pizza.masa = "suave"

    def build_salsa(self):
        self.pizza.salsa = "dulce"

    def build_relleno(self):
        self.pizza.relleno = "jamon y piña"

    def get_pizza(self):
        return self.pizza
from PizzaBuilder import PizzaBuilder
from Pizza import Pizza

class BolognesePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza=Pizza()    

    def build_masa(self):
        self.pizza.masa = "suave"

    def build_salsa(self):
        self.pizza.salsa = "tomate"

    def build_relleno(self):
        self.pizza.relleno = "carne de ternera"

    def get_pizza(self):
        return self.pizza    
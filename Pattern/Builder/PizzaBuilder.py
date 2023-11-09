from .Builder import *

class PizzaBuilder:
    def build_masa(self):
        pass

    def build_salsa(self):
        pass

    def build_relleno(self):
        pass

    def get_pizza(self):
        pass

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
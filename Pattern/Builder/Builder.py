class Pizza:
    def __init__(self):
        self.masa = ""
        self.salsa = ""
        self.relleno = ""
    
    def __str__(self):
        return f"Masa: {self.masa}, Salsa: {self.salsa}, Relleno {self.relleno}"

class Builder:
    def __init__(self):
        self.pizza = None

    def create_new_pizza(self):
        self.pizza=Pizza()    

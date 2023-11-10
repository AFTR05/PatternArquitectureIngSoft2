from Pizza import Pizza
## Builder 

class Builder:
    def __init__(self):
        self.pizza = None

    def create_new_pizza(self):
        self.pizza=Pizza()    

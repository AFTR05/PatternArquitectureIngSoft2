class Pizza:
    def __init__(self):
        self.masa = ""
        self.salsa = ""
        self.relleno = ""
    
    def __str__(self):
        return f"Masa: {self.masa}, Salsa: {self.salsa}, Relleno {self.relleno}"

# Clase pizza con atributos y modificacion de metodo toString
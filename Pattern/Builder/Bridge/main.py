# Archivo principal para probar
from moto import MotoImplementacion
from motos import MotoDeportivaImplementacion, MotoCalleImplementacion
from abstraccion import MotoAbstraccion
from conduccion import ConduccionDiurna, ConduccionNocturna

if __name__ == "__main__":
    moto_deportiva = MotoDeportivaImplementacion()
    moto_calle = MotoCalleImplementacion()

    conduccion_diurna_deportiva = ConduccionDiurna(moto_deportiva)
    conduccion_nocturna_calle = ConduccionNocturna(moto_calle)

    print(conduccion_diurna_deportiva.conducir())
    print(conduccion_nocturna_calle.conducir())

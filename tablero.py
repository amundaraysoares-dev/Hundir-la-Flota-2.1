from nave import Nave
from casilla import Casilla

class Tablero:
    def __init__(self):

        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        #NAVES
        por1 = Nave("Destructor", "portaaviones", 5)
        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        #CASILLAS
        #este es un objeto el cual es un casillero donde almacenaremos
        # 10  filas de 10 casillas para recrear una cuadricua 10x10
        #dentro de cada casilla se almacenara la informacion de si hay un barco o no
        self.casillero = [
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()]
        ]



        # portaaviones
        self.casillero[1][1].nave = por1
        self.casillero[1][2].nave = por1

        # fragatas
        self.casillero[3][3].nave = fra1
        self.casillero[4][3].nave = fra1
        self.casillero[5][3].nave = fra1


        # submarinos
        self.casillero[4][6].nave = sub1

    # DISPARO
    #se encarga de comprobar el disparo y mostrarlo por pantalla
    #tambien llama a la funcion disparo de la clase casilla
    # y le envia la casilla dentro del casillero que esta siendo atacada
    def comprobar_impacto(self, x, y):
        print(f"Impacto en ({x},{y})")
        return self.casillero[x][y].disparar()
En mi codigo he modificado la clase tablero y he creado casilla las cuales se relacionan para gestionar el disparo

en tablero tenemos esta funcion que le enviara la informacion del ataque a la casilla
    
    def comprobar_impacto(self, x, y):
        print(f"Impacto en ({x},{y})")
        return self.casillero[x][y].disparar()
 
y dentro de la clase calsilla utilizara la informacion del ataque para devolver al jugador elestado en el cual se encuentra esa casilla
ya puede ser agua,ya has disparado aqui o que ataque haya ido bien y tenga que recurrir a la clase nave para indicarle que ha recibido un disparo
class Casilla:
   
    def __init__(self):
        self.nave = None
        self.usada = False


    def disparar(self):

     
        if self.usada:
            print("Ya disparaste aquí")
            return None
     
        self.usada = True
       
        if self.nave is None:
            print("Agua")
            return 0
       
        return self.nave.recibir_disparo()

  Y por ultimo en tablero cree casillero que es un conjunto de almacenamientos que se encargan de formar un tablero de 10x10 de casillas
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

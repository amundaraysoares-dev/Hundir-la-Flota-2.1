class Casilla:
    #lo primero es definir los objetos de la clase
    #nave que va a ser none, indicando de base que no hay
    #usada que sera false de base para indicar que esta libre de base
    def __init__(self):
        self.nave = None
        self.usada = False


# esta funcion se encarga de gestionar el disparo con dos posibles opciones
    def disparar(self):

        # primera opcion es que si el objeto usada es true,
        # significa que ya se ha atacado esta casilla y
        # por lo tanto devolvera un mensaje indicando que no se puede
        if self.usada:
            print("Ya disparaste aquí")
            return None
        # si no ha sido usada ignorara la condicion anterior y realizara el disparo
        # tambien convertira la clase usada en true en esa casilla
        self.usada = True
        #La segunada es que si el disparo da en ina casilla la cual esat vacia y no hay nuinguna nave dentro
        # va a devolver el estado de agua y a mostrarlo por pantalla
        if self.nave is None:
            print("Agua")
            return 0
        #por ultimo va a enviarle el resultado del disparo a la nave en caso de dar
        #llamando a la funcion de la clase nave recibir_disparo
        return self.nave.recibir_disparo()
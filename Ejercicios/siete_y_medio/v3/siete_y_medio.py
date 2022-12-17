from juego import Juego
import utilidades as utl
class SieteYMedio(Juego):
    
    def __init__(self):
        Juego.__init__(self,"Siete y medio")
        self.__Jugadores = []
        self.__baraja = utl.cartas

    def inicio(self):
        super().inicio()

# getters y setters
    @property
    def Jugadores(self):
        return self.__Jugadores
    @Jugadores.setter
    def Jugadores(self,Jugadores):
        self.__Jugadores = Jugadores

    @property
    def baraja(self):
        return self.__baraja
    @baraja.setter
    def baraja(self,baraja):
        self.__baraja = baraja
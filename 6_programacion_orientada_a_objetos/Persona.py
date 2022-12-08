class Persona:
    # constructor, no me construyes si no tengo nombre
    def __init__(self,nombre,edad,estatura,mascota=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__estatura = estatura
        self.mascota = mascota
        
    def saludar(self):
        print(f"Hola soy {self.__nombre}")
    
    def hablar(self,mensaje):
        print(f"{self.__nombre}: {mensaje}")
    
    def adoptarMascota(self,mascota):
        self.mascota = mascota
    
    def quien_es_mi_mascota(self):
        print("mascota:",self.mascota.que_soy())

    def __str__(self):
        return f""" 
******* {self.__nombre} ****** 
edad:{self.__edad}
estatura: {self.__estatura}
"""
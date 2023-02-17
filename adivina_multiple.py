
import random
import os

# from adivina import contadorIg 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# usuario = {}

# def new_usuario(id):
#     id = id
#     nombre = str(input("Cual es tu nombre = "))
#     contador = 0 
#     muertes = 0
#     escapatorias = 0
#     usuario[int(id)] = {"nombre": nombre, "contador" : contador, "muertes" : muertes , "escapatorias" : escapatorias }

# if id in usuario:
#     pass
# else:
#     new_usuario(id)
class Game:
    
    salir = False
    contador = 0
    numero = random.randint(0,9999)
    elegido = ""

# print(numero)
    def contadorIg(self,ramdom,escogido):
        self.ramdom = str(ramdom)
        self.escogido = f"{escogido:04d}"
        self.medir = len(self.ramdom)
        self.contadorInterno = 0
        for indice in range(0,self.medir):
            if self.ramdom[indice:indice+1] == self.escogido[indice:indice+1]:
                self.contadorInterno+=1
        return self.contadorInterno

    def jugar(self,contador,numero):
        while contador < 15:

            self.elegido = int(input("Introduce un numero = "))
            cls()
            print(f"escogiste {self.elegido} y {numero}")
            if numero < self.elegido:
                tamaño = "pequeño"
                # print("El número que has introducido es mas grande ")
            elif numero > self.elegido:
                tamaño = "grande"
                # print("El número que has introducido es mas pequeño ")
            elif numero == self.elegido:
                print("ENHORABUENA")
                break
            contador+=1
            coincidencias = self.contadorIg(numero,self.elegido)
            print(f"El numero es mas {tamaño} y hay {coincidencias} coincidencias")
            # time.sleep(1)
            
        else:
            print("Muerto")

    # def __init__(self):
    #     self.jugar(self.contador,self.numero)
# n = Game()

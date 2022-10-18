import yaml
from pprint import pprint
import random
import matplotlib.pyplot as plt


#Aqui creo todos los diccionarios necesarios para hacer el ejercicio
d = { 'moneda': {
    'cara':{},
    'cruz': {}
},
      'dados':{}
}



#La lista que creo aqui solo sirve para la funcion de tirarmonedas
# que lo que hago es hacer que coja una opcion entre cara y cruz
moneda = ["cara","cruz"]
def tirarmonedas():
    return random.choice(moneda)
#Esta funcion solo la utilizo para sacar el valor del dado del 1 al 6 realmente se puede utilizar en
# otro sitio pero me apetecia hacerlo en una funcion para que quedase mas bonito
def tiradaDado():
    return random.randint(1, 6)



#Aqui empieza el main
if __name__ == "__main__":

#Estos dos primeros for son para inicializar el diccionario d uno para la moneda y otro para el dado
    for x in range(11):
        d['moneda']['cara'][x] = 0
        d['moneda']['cruz'][x] = 0

    for y in range(3,19):
        d['dados'][y] = 0
#Aqui empieza el for uqe se va a ejecutar un millon de veces para realizar los experimentos
    for _ in range(1000000):
        #Aqui inicializo las variables de los contadores
        contCara=0
        contCruz=0
        dado=0
        #Este primer for sirve para tirar la moneda 10 veces, lo que hace es usar la funcion
        #tirarmonedas para que saque una entre cara o cruz y dependidendo de la string suma uno a cara o a cruz
        for _ in range(10):
            if(tirarmonedas() == "cara"):
                contCara=contCara+1
            else:
                contCruz=contCruz+1

        #Aqui suma uno en la posicion de la cantidad de veces que se ha sacado uno u otro
        #Esto se puede comprobar por que cuando se imprime por pantalla la cantidad de
        #veces que se saque cara en 0 tiene que ser el mismo numero que se saca en cruz 10 y asi con todos los numeros
        d['moneda']['cara'][contCara] += 1
        d['moneda']['cruz'][contCruz] += 1

        #Este es el bucle de los dados
        for _ in range(3):
            dado += tiradaDado()
        #Aqui añodo uno a la cantidad que ha salido en dado
        d['dados'][dado] += 1


#Este printo solo sirve para imprimir por pantalla el diccionario
    pprint(d)


#Cada bloque que empieza por plt.figures es para una grafica

#Caras
    plt.figure()
    Ccaras= d['moneda']['cara'].keys()
    Vcaras= d['moneda']['cara'].values()
    plt.plot(Ccaras,Vcaras)
    plt.xlabel("Caras")
    plt.show()

#Cruces
    plt.figure()
    Ccruz= d['moneda']['cruz'].keys()
    Vcruz= d['moneda']['cruz'].values()
    plt.plot(Ccruz,Vcruz)
    plt.xlabel("Cruces")
    plt.show()

#Dados
    plt.figure()
    Cdado= d['dados'].keys()
    Vdado= d['dados'].values()
    plt.plot(Cdado,Vdado)
    plt.xlabel("Dado")
    plt.show()
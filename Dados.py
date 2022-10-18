import yaml
from pprint import pprint
import random
import matplotlib.pyplot as plt

d = { 'moneda': {
    'cara':{},
    'cruz': {}
},
      'dados':{}
}

moneda = ["cara","cruz"]
def tirarmonedas():
    return random.choice(moneda)

def tiradaDado():
    return random.randint(1, 6)

if __name__ == "__main__":

    for x in range(11):
        d['moneda']['cara'][x] = 0
        d['moneda']['cruz'][x] = 0

    for y in range(3,19):
        d['dados'][y] = 0

    for _ in range(1000000):
        contCara=0
        contCruz=0
        dado=0
        for _ in range(10):
            if(tirarmonedas() == "cara"):
                contCara=contCara+1
            else:
                contCruz=contCruz+1
    
        d['moneda']['cara'][contCara] += 1
        d['moneda']['cruz'][contCruz] += 1
        for _ in range(3):
            dado += tiradaDado()
        
        d['dados'][dado] += 1

    pprint(d)

    plt.figure()
    Ccaras= d['moneda']['cara'].keys()
    Vcaras= d['moneda']['cara'].values()
    plt.plot(Ccaras,Vcaras)
    plt.xlabel("Caras")
    plt.show()

    plt.figure()
    Ccruz= d['moneda']['cruz'].keys()
    Vcruz= d['moneda']['cruz'].values()
    plt.plot(Ccruz,Vcruz)
    plt.xlabel("Cruces")
    plt.show()

    plt.figure()
    Cdado= d['dados'].keys()
    Vdado= d['dados'].values()
    plt.plot(Cdado,Vdado)
    plt.xlabel("Dado")
    plt.show()
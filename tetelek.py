import random

def atlag(letszam=20, hatar=5, tizedes=2):
    lista = []
    for i in range(letszam):
        lista.append(random.randrange(1, hatar+1))
    print(lista)
    osszeg = 0
    for i in range(len(lista)):
        osszeg = osszeg + lista[i]
    print(f"Az osztály átlaga: {osszeg/len(lista):.{tizedes}f}")

def osszefuzes(letszam=4, szoveg="Név: "):
    lista = []
    for i in range(letszam):
        lista.append(input(szoveg))
    print(lista)
    szo = ""
    for i in range(len(lista)):
        szo = szo + " " + lista[i]
    print(szo)

def megszamlal(also_hatar, felso_hatar, oszthato):
    db = 0
    for i in range(also_hatar, felso_hatar+1):
        if i % oszthato == 0:
            db += 1
    print(f"Darabszám: {db}")

def veletlen(also_hatar, felso_hatar, szam):
    lista = []
    db = 0
    for i in range(5):
        lista.append(random.randrange(also_hatar, felso_hatar))
    for i in range(len(lista)):
        if lista[i] == szam:
            db += 1
    print(lista)
    print(f"Darabszám: {db}")
import Renszarvas


def beolvas():
    lista = []
    beFajl = open("fajlok/Mikulasszan.txt", "r", encoding="utf-8")
    adatokListaja = beFajl.readlines()
    # print(adatokListaja)
    for index in range(1, len(adatokListaja), 1):
        if not ("Santa Claus" in adatokListaja[index]):
            daraboltSor = adatokListaja[index].split("@")
            # print(daraboltSor)
            renszarvas = Renszarvas.Renszarvas(daraboltSor[0], daraboltSor
            [1], daraboltSor[2], daraboltSor[3])
            print(renszarvas)
            lista.append(renszarvas)
    beFajl.close()

    return lista


def angolMegfelelo(nev: str, lista: list):
    index = 0
    talalat = True
    while index < len(lista) and talalat:
        if lista[index].nevMagyar == nev:
            # print(szarvas.nevAngol)
            talalat = False
        index += 1

    if not talalat:
        print(f"szarvas angol neve:{lista[index - 1].nevAngol}.")
    else:
        print("Nincsen ilyen rénszarvas")


def mikulasSzam(lista: list):
    db = 0
    index = 0
    while index < len(lista):
        daraboltLeiras = lista[index].leiras.split(" ")
        # print(daraboltLeiras)
        index2 = 0
        while index2 < len(daraboltLeiras):
            if daraboltLeiras[index2] == "Mikulás":
                db += 1
            index2 += 1
        index += 1
    print(f"A mikulás szó előfurdulásánal száma: {db}.")

def atlagMagassag(lista):
    osszeg = 0
    index = 0
    while index < len(lista):
        osszeg += lista[index].magassag
        index +=1

    if len(lista) == 0:
        print("A szarvasok átlag magassága: 0.")
    else:
        atlag = osszeg / len(lista)
        print(f"A szarvasok átlag magassága: {atlag:.2f}")

def parosHelyenRepuloSzarvasok(lista):
    print("A páros számú helyeken répülő szarvasok nevei: ", end="")
    index = 0
    hely = 0
    while index < len(lista):
        if lista[index].hely%2==0:
            print(lista[index].nevMagyar+" ", end="")
        index +=1
    print("")


def leghosszabbLeiras(lista):
    maxErtek = len(lista[0].leiras)
    maxIndex = 0
    index = 0
    while index < len(lista):
        if len(lista[index].leiras) > maxErtek:
            maxErtek = (lista[index].leiras)
            maxIndex = index
        index += 1
    print(f"A leghosszabb leírása{lista[maxIndex].nev} van (hossza: {maxErtek} karakter).")

def hetes():
    szarvasokListja = beolvas()
    for szarvas in szarvasokListja:
        print(szarvas.kiir())

    print(f"A rénszarvasok száma:{len(szarvasokListja)}")

    angolMegfelelo("Pompás", szarvasokListja)
    mikulasSzam(szarvasokListja)
    atlagMagassag(szarvasokListja)
    parosHelyenRepuloSzarvasok(szarvasokListja)
    leghosszabbLeiras(szarvasokListja)
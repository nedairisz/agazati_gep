"""
A gep.txt forrásállomány, gépek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A gep.txt állomány szerkezete:
·         id (azonosító): pl: 1
·         hely (terem azonosítója): pl.: T403
·         típus (a gép típusát jelöli): pl.: asztali
·         ipcim (a gép ipcíme): pl.: 192.168.2.1
Az állomány első sora a mezőneveket tartalmazza felkiáltó jellel elválasztva.

A megoldás mintája:
III/A, B:
            A gépek száma: 76.
III/C:
           A páros teremszámú termek azonosító átlaga: 39.
III/D:
            A legkisebb asztali gép azonosítója: 1, helye: T403.

⦁	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) 
    a gep.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, 
    ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az 
    állomány első sora az adatok fejlécét tartalmazza! (7p)
⦁	Írassa ki a gépek számát a mintának megfelelően a konzolra! A metódus neve 
    legyen gepek_szama! (2p)
⦁	Határozza meg és írassa ki a konzolra a minta szerint, hogy a páros 
    teremszámú termeknek mi az azonosító átlaga. A metódus neve legyen atlag! (4p)
⦁	Írassa ki konzolra a mintának megfelelően a legkisebb azonosítójú asztali gép 
    azonosítóját és helyét (ha több is van, akkor az első legkisebb adatait). 
    A metódus neve legyen legkisebb!  (4p)
"""
from Gep import Gep

def beolvasas():
    fajl=open("gep.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close

    lista=[]
    for i in range(0, len(nyers_lista), 1):
        sorok= nyers_lista[i]
        adat_sor= sorok.strip().split("!")
        id=int(adat_sor[0])
        hely=str(adat_sor[1])
        tipus=str(adat_sor[2])
        ipcim=str(adat_sor[3])
        gep=Gep(id, hely, tipus, ipcim)
        lista.append(gep)
    
    return lista

def gepek_szama(lista):
    szamlalo:int=0
    for i in range(0,len(lista),1):
        szamlalo+=1
    return szamlalo

def atlag(lista):
    terem_szamlalo:int=0
    id_osszeg:int=0
    for i in range(0, len(lista), 1):
        terem= int(lista[i].hely.strip("T"))
        if terem%2==0:
            terem_szamlalo+=1
            id_osszeg+= lista[i].id
    azonosito_atlag=id_osszeg/terem_szamlalo
    return azonosito_atlag

def legkisebb(lista):
    legkisebb_id=100
    legkisebb_hely_index=0
    for i in range(0, len(lista), 1):
        if lista[i].tipus=="asztali":
            if legkisebb_id > lista[i].id:
                legkisebb_id = lista[i].id
                legkisebb_hely_index= (lista[i].hely)

    print(f"A legkisebb asztali gép azonosítója: {legkisebb_id}, helye: {legkisebb_hely_index}.")


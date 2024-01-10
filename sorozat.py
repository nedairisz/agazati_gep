"""
II/A, B, C:
           	20*-28*124*166*15*-188*174*243*20*28*-124*166*15*-188*174
II/D, E:
           	Tízzel osztható számok száma: 1.  	
            kimutatas.txt tartalma:
II/F:
            Tízzel osztható számok száma: 1. 

⦁	Írasson ki a konzolra csillag jellel (*) elválasztva 15 számból álló véletlen számsorozatot
     [-90,500] zárt intervallumon a mintának megfelelően! (4p)
⦁	A generált értékeket tárolja lista adatszerkezetben! (1p)
⦁	A * jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
⦁	Írjon függvényt oszthatoak_szama néven, amiben számolja meg, hogy hány olyan elem van, 
    ami tízzel osztható. A visszatérési érték legyen egy egész szám, a függvény bemenete a 
    lista! (3p)
⦁	Az oszthatoak_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, 
    amit konzolra_ir nevű metódusban fogalmazzon meg! (2p)
⦁	Az oszthatoak_szama függvény eredményét írassa ki a mintának megfelelően a kimutatas.txt 
    nevű fájlba, amit fajl_ir nevű metódusban fogalmazzon meg! (2p)
"""
import random

def szam_generalas():
    lista=[]
    print(f"\t", end="")
    for i in range(0,15,1):
        szam=random.randint(-90,500)
        lista.append(szam)
        if i == 14:
            print(szam, end="")
        else:
            print(szam, end="*")
    return lista

def oszthatoak_szama(lista):
    i:int =0
    tizzel_oszthato:int=0
    while i < len(lista):
        if int(lista[i])%10==0:
            tizzel_oszthato+=1
        i+=1
    return tizzel_oszthato

def konzolra_ir(tizzel_oszthato):
    print(f"\tTízzel osztható számok száma: {tizzel_oszthato}")

def fajl_ir(tizzel_oszthato):
    fajl = open("kimutatas.txt", "w", encoding="utf-8")
    fajl.write(f"II/F:\tTízzel osztható számok száma: {tizzel_oszthato}")
    fajl.close()
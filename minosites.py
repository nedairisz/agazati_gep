""" 
I/A:
Múzeum neve: Magyar Zene Háza
Látogató neve: Nagy Zoltán
Értékelés (1-20): 16
 
I/B:
Köszönjük az értékelést! 

A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
    múzeum neve, látogató neve és értékelés!  (2p)
B.	A program az adatbekérés után írja ki a következők egyikét: (a mintának megfelelően – 1p)
    Ha az értékelés nem a megfelelő határokon belül lett megadva 
    ( [1,20], zárt intervallum értendő):
⦁	Amennyiben negatív vagy 0 számot adott meg: “Az értékelés nem lehet negatív vagy 0!”,
⦁	Amennyiben 20 feletti egész számot adott meg: “20 pont feletti értékelés nem elfogadható!”
⦁	Helyes pont-adat esetén: “Köszönjük az értékelést!” 
Feltételezzük, hogy csak egész számokat adnak meg. (4p + 1p)
"""

def bekeres():
    muzeum:str= str(input("Múzeum neve: "))
    latogato:str=str(input("Látogatóneve: "))
    ertekeles:int=int(input("Értékelés (1-20): "))
    print("I/B:")
    if ertekeles<1:
        print("Az értékelés nem lehet negatív vagy 0!")
    elif ertekeles>20:
        print("20 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")
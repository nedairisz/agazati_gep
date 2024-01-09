import minosites
import sorozat
import helyzet

""""""
print("I/A:")
minosites.bekeres()

print("II/A, B, C:")
lista= sorozat.szam_generalas()
print("\nII/D, E:")
tizzel_oszthato=sorozat.oszthatoak_szama(lista)
sorozat.konzolra_ir(tizzel_oszthato)
print("kimutatas.txt tartalma:")
print("II/F:")
sorozat.fajl_ir(tizzel_oszthato)

print("III/A, B:")
lista=helyzet.beolvasas()
szamlalo= helyzet.gepek_szama(lista)
print(f"A gépek száma: {szamlalo}")
print("III/C:")
azonosito_atlag=helyzet.atlag(lista)
print(f"A páros teremszámú termek azonosító átlaga: {azonosito_atlag}")
print("III/D:")
helyzet.legkisebb(lista)


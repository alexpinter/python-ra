"""
Adott a classroomon egy fájl, a 'szavak.txt', amelyben szavak találhatók 
egyes- és többesszámban.
Számold meg hány szó van a fájlban egyesszámban és mennyi többesszámban.
Írd ki a képernyőre az eredményeket!
Használj függvényeket a megvalósítás során!
"""
def tobbesszam(fajl):
    tobbes=0
    sorok=fajl.read()
    szavak=sorok.split("\n")
    for szo in szavak:
        if szo[-1]=="k":
            tobbes+=1
    fajl.seek(0)
    egyes=len(fajl.readlines())-tobbes
    print("A fajlban %d darab többesszám van!" %tobbes)
    print("A fájlban %d darab egyesszám van!" %egyes)

fajl=open("szavak.txt", "r")
tobbesszam(fajl)

"""
Egészitd ki a feladatot úgy, hogy kiírd a képernyőre azokat a szavakat a 
fájlból amelyekben legalább 2db 'e' betű található és többesszámban van.
"""
def ebetu(fajl):
    fajl.seek(0)
    sorok=fajl.readlines()
    for szo in sorok:
        if szo.count('e')>=2 and (szo[-1]=='k' or szo[-2]=='k'):
            print(szo)
            
ebetu(fajl)
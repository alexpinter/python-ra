import csv
letszam =  int(input("add meg az osztály létszámát"))


osztalyzatok = {}



for i in range(letszam):
    osztalyzatok.update({i: {"nev": input(f"ad meg az {i+1} nevét"),"osztalyzat": input(f"add meg {i+1} osztályzatot" )}})
   
szj= int(100/letszam)
n=[0,0,0,0,0]
for i in osztalyzatok:
    n[int(osztalyzatok[i]["osztalyzat"])]+=szj
print(n)   
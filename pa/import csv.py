import csv

with open("C:\\Users\\szakinf\\Documents\\pa\\adatok.csv" ) as f:
    olvasott = csv.reader(f)
    for sor in olvasott:
        print(sor)

with open("uj_adatok.csv", "w" , newline='') as f:
    irott = csv.writer(f, delimiter=";")
    irott.writerow(["sorszám","vezetáknév", "keresztnév","szül év"])
    irott.writerow([1, "Kiss", "János", 1986])

with open("jatekos.csv", "w") as f:
    oszlopok=["jatekos_neve", "rating"]
    iro=csv.Dictwriter(f , fieldnames=oszlopok)
    iro.writeheadet()
    iro.writerow({'jatekos_neve':'Thogelle Sándor','rating':99})

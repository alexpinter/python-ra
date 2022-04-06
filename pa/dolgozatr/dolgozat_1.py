'''
Készíts egy programot, amely létrehoz egy nyilvántartást. A táblázatot írd ki egy csv fájlba.
A program kérje be a felhasználótól a keresztnevet, valamint hogy heti hány órát dolgozott. 
Ez táblázatos formában írd ki a fájlba. A táblázat harmadik oszlopában pedig a ledolgozott óraszámok százalékos 
aránya kerüljön, amennyiben heti 40 óra számít 100%-nak. Használj függvényeket a megvalósítás során! 
Kérj be legalább 5 adatot!
'''

f=open("C:\\Users\\szakinf\\Documents\\pa\\dolgozatr\\nyilvantartas.csv", "w")

f.writelines("Keresztnév;Ledolgozott órák;Százalékosan\n")

def adat(f):
    keresztnevek=[]
    orak=[]

    for i in range(5):
        keresztnevek.append(input("Adja meg a keresztnevét: "))
        orak.append(input("Adja meg hány órát dolgozott a héten: "))
    
    for i in range(len(keresztnevek)):
        f.writelines(str(keresztnevek[i])+";"+str(orak[i])+";"+str(int(orak[i])/40*100)+"\n")

adat(f)
f.close    
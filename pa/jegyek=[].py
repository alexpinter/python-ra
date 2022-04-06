jegyek=[]

def osztalyzat(pont):
    pont=int(pont)
    if (pont>=0 and pont<=15):
        jegyek.append(1)
        print("Ez a pont elégtelen (1)")
    elif (pont>=16 and pont<=25):
        jegyek.append(2)
        print("Ez a pont elégséges (2)")        
    elif (pont>=26 and pont<=35):
        jegyek.append(3)
        print("Ez a pont közepes (3)")
    elif (pont>=36 and pont<=45):
        jegyek.append(4)
        print("Ez a pont jó (4)")
    elif (pont>=46 and pont<=50):
        jegyek.append(5)
        print("Ez a pont jeles (5)")
    else:
        pass

def atlag(jegyek):
    osszeg=0
    for i in range(len(jegyek)):
        osszeg=osszeg+jegyek[i]
    atlag=float(osszeg/len(jegyek))
    return atlag

def jegyDarab(jegyek):
    darab=[]
    for i in range(1,6):
        darab.append(jegyek.count(i))
    return darab

def parossag(jegyek):
    parossag=[0, 0]     #páratlan, páros
    for i in range(len(jegyek)):
        if jegyek[i]%2:
            parossag[0]+=1
        elif not jegyek[i]%2:
            parossag[1]+=1
        else:
            pass
    return parossag

def bukas(jegyek):
    elegtelen=jegyek.count(1)
    bukas=float((elegtelen/len(jegyek))*100)
    print("Az osztály bukási aránya: %f" %bukas)

for i in range(20):
    pont=input("Add meg a diák pontszámát: ")
    osztalyzat(pont)

atlag=atlag(jegyek)
print("Az osztály átlaga: %f" %atlag)
darab=jegyDarab(jegyek)
print("Az egyes osztályzatok darabszáma rendre: ")
print(darab)
parossag=parossag(jegyek)
print("""Páratlan osztályzatok száma: %d \n
Páros osztálytatok száma: %d""" %(parossag[0], parossag[1]))
bukas(jegyek)
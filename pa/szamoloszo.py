fajl =  open("C:\\Users\\szakinf\\Documents\\pa\\szavak.txt", "r", encoding="utf-8")

def szamlalo():
    szoveg = fajl.readlines()
    n = 0
    e = 0
    t = 0
    lista = []
    for i in szoveg:
        if i[-2]=="k":
            n+=1
        elif i[-1]=="k":
              n+=1     
        else:
            e+=1

    for szo in szoveg:
        if szo.count('e') >= 2:
            lista.append(szo)
            t+=1

    print("%ddb többesszámban lévő  szó van a fájlban." %n)
    print("%ddb  egyesszámban lévő szó van a fájlban." %e)
    print("%ddb e betűt 2x  tartalmazó és többesszámban lévő szó van a fájlban" %t)
    print(lista)
szamlalo()
fajl.close()

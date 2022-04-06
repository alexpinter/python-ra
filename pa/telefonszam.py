def ellenoriz(szam):
    while not (len(szam)==12 or len(szam)==13):
        print("A szám hossza nem megfelelő!")
        szam=input("""Adj meg egy telefonszámot!
        A formailag elfogadott számok: +36XXYYYYYYY vagy 006XXYYYYYYY""")

    while not szam[0:3]=='+36' or szam[0:4]=='0036':
        print("A szám '+'-al vagy '00'-val kell, hogy kezdődjön!")
        print("A szám hossza nem megfelelő!")
        szam=input("""Adj meg egy telefonszámot!
        A formailag elfogadott számok: +36XXYYYYYYY vagy 006XXYYYYYYY""")

    seged=True
    for i in range(-1, 11, -1):
        if szam[i].isdecimal():
            pass
        else:
            print("Nem megfelelő szám!")
            seged=False
            break
        while not seged:
            szam=input("""Adj meg egy telefonszámot!
            A formailag elfogadott számok: +36XXYYYYYYY vagy 006XXYYYYYYY""")
    return szam        

szam=input("""Adj meg egy telefonszámot!
A formailag elfogadott számok: +36XXYYYYYYY vagy 006XXYYYYYYY""")
szam=ellenoriz(szam)
if szam[-9:-7]=='20':
    print("Az adott szám Telenor szolgáltatóhoz tartozik!")
elif szam[-9:-7]=='30':
    print("Az adott szám Telekom szolgáltatóhoz tartozik!")
elif szam[-9:-7]=='50':
    print("Az adott szám Digi szolgáltatóhoz tartozik!")
elif szam[-9:-7]=='70':
    print("Az adott szám Vodafone szolgáltatóhoz tartozik!")
elif szam[-9:-7]=='40':
    print("Az adott szám Kékszám!")
elif szam[-9:-7]=='80':
    print("Az adott szám Zöldszám!")
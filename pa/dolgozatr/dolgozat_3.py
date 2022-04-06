'''
Adott az auto.txt fájl. Keresd meg mindazokat a mondatokat amelyekben szerepel a “méter” szó és írasd ki őket a képernyőre. 
Használj függvényeket a megvalósítás során!
'''

f=open("C:\\Users\\szakinf\\Documents\\pa\\dolgozatr\\auto.txt", "r", encoding="utf-8")

def meter(f):
    mond=f.readlines()

    for i in range(len(mond)):
        mond[i]=mond[i].split('.')
        for x in mond[i]:
            if "méter" in x:
                print(x)
meter(f)
f.close
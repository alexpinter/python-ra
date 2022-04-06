'''
Adott egy szavak.txt nevű fájl, amely szavakat tartalmaz. 
Keresd meg mindegyik szót, amelynek a középső betűje mássalhangzó és írasd ki a képernyőre. 
Vedd figyelembe a sor végi sortöréseket is. A páros számú szavakat hagyd figyelmen kivűl! 
Használj függvényeket a megvalósítás során!
'''
f=open("C:\\Users\\szakinf\\Documents\\pa\\dolgozatr\\szavak.txt", "r", encoding="utf-8")

def msh(f):
    szavak=f.readlines()

    massal=["b","c","cs","d","dz","dsz","f","g","h","j","k","l","ly","m","n","ny","p","q","r","s","sz","t","ty","v","w","x","y","z","zs"]
    koz=[]
    sd=[]
    for i in szavak:
        i=i.replace('\n', '')
        if len(i)%2!=0:
            kozepe=len(i)//2
            if i[kozepe] in massal:
                print(i)
msh(f)
f.close
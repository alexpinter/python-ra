f=open("szavak.txt", "r", encoding="utf-8")
def mgh_msh_szazalek(f):
    mgh=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
    msh=["q","w","r","t","z","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m","ly","cs","dz","dzs","ny","gy"]
    
    szavak=f.readlines()
    magan=[]
    massal=[]
    for betu in szavak:
        for j in betu:
            if j in mgh:
                magan.append(j)
            elif j in msh:
                massal.append(j)
    
    a=len(magan)
    b=len(massal)
    osszes=a+b
    mg=a/osszes*100
    ms=b/osszes*100

    print("A fájlban "+str(len(magan))+" magánhangzó és "+str(len(massal))+" mássalhangzó van")
    print("A betűknek %f százaléka magánhangzó"%mg)
    print("A betűknek %f százaléka mássalhangzó"%ms)
mgh_msh_szazalek(f)

f.close()
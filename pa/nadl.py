
fajl =  open("C:\\Users\\szakinf\\Documents\\pa\\nemzeti-dal.txt", "r", encoding="utf-8")

sorok=fajl.readlines()   
sordb=[] 
sorokszama=len(sorok) 
for i in range(sorokszama):
    sordb.append(0) 
db=0 
osszdb=0 
a= []
i=0 
for sor in sorok: 
    szavak=sor.split(" ")     
    for szo in szavak: 
        if "\n" in szo: 
            szo=szo.replace("\n","")
        if 'a' in szo:
            a.append(szo)
        if len(szo)<5:
            db+=1
    sordb[i]=db
    i+=1 
    db=0
for i in range(len(sordb)): 
    print("Az %d. sorban %d keresett szó van!" %(i, sordb[i]))
    osszdb+=sordb[i]

print("A teljes szövegben %d db keresett szó van!" %osszdb) 
print(a)











    
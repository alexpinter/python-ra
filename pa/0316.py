fajl =  open("C:\\Users\\szakinf\\Documents\\pa\\03-16.txt", "r", encoding="utf-8")

sorok = fajl.readlines() #a "sorok" egy lista
ujfajl = open("03-16-uj.txt", "a")
for sor in sorok:
    ujsorok = sor.split(".")
    if len(ujsorok)>1:
        ujsorok.pop()
    for ujsor in ujsorok:
        ujsor = ujsor.lstrip()
        ujfajl.write(ujsor)
        ujfajl.write("\n")
     



maganh    = ["e","u","i","o","a","y"]
darab = 0
for sor in sorok:
    for i in sor:
        if i in maganh:
            darab+= 1


maganha= "aeiouAEIOU"
db=0
f = open("03-16-uj.txt", "r").readlines()
sorok = f.readlines()
for sor in sorok:
    for kar in sor:
        if kar in maganha:
            db+=1
print(db)
ujfajl.close()
fajl.close()  
print("a szövegben %d db maganhangzo van" %darab)
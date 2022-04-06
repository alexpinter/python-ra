fajl =  open("C:\\Users\\szakinf\\Documents\\pa\\ebetu.txt", "r", encoding="utf-8")

sorok = fajl.readlines()
ujsorok =[]
maganh    = ["e","u","i","o","ő","ú","ö","ü",'ó',"a","é","á ","ű","í"]


for sor in sorok:
    for i in sor:
        if i in maganh:
            sor = sor.replace(i, "")
    ujsorok.append(sor)
fajl.close()
print(ujsorok)



ujfajl = open("massalhangzok.txt", "w")
ujfajl.writelines(ujsorok)
ujfajl.close()










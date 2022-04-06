'''
import random 
n=0
tomb=[]
for i in range (100):
    tomb.append(random.randint(1,100))
                     
for j in tomb:
    if j%2==0:
        print(j, end=" ")
        n+=1
print("A páros számok darabszáma: %d " %n)

for x in range(100):
    if x<(len(tomb)-1):
        if tomb[x]<tomb[x+1]:
            print(tomb[x], end=" ")


import random
tomb=[]
for i in range (100):
    tomb.append(random.randint(-50,50))
    
for k in range(100):
 if   tomb[k]<0:
     tomb[k]=abs(tomb[k])

for j in tomb:
     if j<0 and(not j%2==0):
         print(j)


tomb=[]
for i in range(10):
    szam=(int(input("adj meg egy számot")))
    while szam in tomb:     
        szam=(int(input("Ez a szám már létezik. Adj meg egy újat:")))
    tomb.append(szam)

for i in range (len(tomb)-1,1,-1):
    for j in range(i-1):
        if tomb[j]>tomb[j+1]:
            temp=tomb[j+1]
            tomb[j+1]=tomb[j]
            tomb[j]=temp
            
print(tomb)


for i in range(1,len(tomb)):
    kulcs=tomb[i]
    j=i-1
    while j>=0 and tomb[j]>kulcs:
        tomb[j+1]=tomb[j]
        j-=1
    tomb[j+1]=kulcs
    
print(tomb)


import random

tomb=[]
segedtomb=[]
for i in range (99):
    tomb.append(random.randint(0,1000))

print(tomb)

for i in range(int(len(tomb)/2)-1)
    segedtomb.append(tomb[i])
    tomb.remove(tomb)

import random

tomb=[]
for i in range (99):
    tomb.append(random.randint(0,1000))
print(tomb)

fele=int(len(tomb)/2)
print(fele)
for i in range(fele-1):
    tomb.sort()
    
    
   
    
    
lista= [ 'alma' ,'pálinka ', 'kerítésszaggató', 'Bicska' ,'körte']
print(lista)
ujlista=[2, 'pitypang' , 3.18 , 'hey google']
print(ujlista)
print(lista[2])
print(lista[:3])
print(lista[-1]) #az utolsó elem
print(lista[-4]) #hátulról a 4. elem
print(lista[-2][:3])

lista= [ 'alma' ,'pálinka ', 'kerítésszaggató', 'Bicska' ,'körte']
print(lista)
ujlista=[2, 'pitypang' , 3.18 , 'hey google']
print(ujlista)
print(lista[2])
print(lista[:3])
print(lista[-1]) #az utolsó elem
print(lista[-4]) #hátulról a 4. elem
print(lista[-2][:3])
szamok=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(szamok[1:-1:3])
lista.append('barack')
print(lista[-1])
lista.append('alma')
print(lista)
lista.remove('alma')
print(lista)

lista.sort() #ascii szerint a nagybetuk vannak elol
print(lista)


ujlista.sort() #kulombozo tipusokat nem tud sortolni
print(ujlista)

lista.reverse()
print(lista)

print(lista[2].count('a'))
print(szamok.count(1))
print(lista.index('Bicska'))
mondat=" a kockáztok és mellékhatások tekintetében olvas l rohadj meg csinálj amit akarsz!"
szavak = mondat.split() #szóközök  menten feldrabolj a a sztringet
print(szavak)
print(" ".join(szavak))

#bejárj a listaelemeit és hozzá rendeli az ujlistahoz
ujlista2 = [x for x in lista]
print(ujlista2) #newlist = [kifejezés for elem in lista]
#az alma kivételével mindent hozzárendel 
ujlista3= [elem for elem in lista if elem!='alma'] #nottal is mukodik
print(ujlista3)





szamok2 =[x for x in range (5,50,3)] #belerakja a listába  a sztámkat 5-50 között 3 as ával

print(szamok2)




adatlopas=[]
while len(adatlopas)<29:
    adatlopas.append(str(input("Adja meg a teljes nevét!")))
    adatlopas.append(str(input("Adja meg a szül. helyét!")))
    adatlopas.append(str(input("Adja meg az anyja nevét! ")))

adatlopas.sort()
print(adatlopas)


adatok=[]
for i in range(5):
    adatok.append(str(input("név: "))+","+str(input("szül. hely: "))+", "+str(input("anja neve: ")))

adatok.sort()
print(adatok)

szamlista=[]
for i in range(10):
    szamlista.append(input("adj meg egy elemet:"))

ujlista=[x for x in szamlista if type(x)==int]
print(ujlista)

tomb=[]
Itomb=[]

for i in range(10):
    inpuut=(input("Add meg a következő értéket:"))
    try:
        if (float(inpuut)%1!=0):
            tomb.append(float(inpuut))
        elif (int(inpuut)%1==0):
            tomb.append(int(inpuut))
            Itomb.append(int(inpuut))
    except:
            tomb.append(str(inpuut))
print(Itomb)




import random
lista=[random.randint(1,30)for i in range (10) ]
eredmeny=[(i^2) for i in lista]
print(lista)
print(eredmeny)

import random

lista=[]
for i in range(10):
    lista.append(random.randint(1,30))

ujszamok=[x**2 for x in lista]
print(lista, "\n", ujszamok)

lista=[[1, 2, 310, 4, 5],["alma", "körte", "szilva", "barack", "banán"]]
print(lista[1][-1])
print(lista[0][2][1])

    
  
 for x in lista[0][x][0]:
        if str(x)<'M':
        print(x)


      
print(lista[0][0][0])


lista=[[],[],[],[]]
for i in range (2):
    lista[0].append(input("adja meg a nevét:"))
    lista[1].append(input("adja meg a születési helyét:"))
    lista[2].append(input("adja meg az anyja nevét:"))
    lista[3].append(int(input("adja meg a születéi évét:")))
print("személyek [A-L]")
for i in range(len(lista[0])):
     if lista[0][i][0] <'M':
         print ("név: %s" %lista[0][i])
         print("születési hely: %s" %lista[1][i])
         print("Anyja neve: %s" %lista[2][i])
         print("születési éve: %d" %lista[3][i])



for x in lista[3]:
    lista[3].sort()
         
        print("születési éve: %d" %lista[3][i])






print("hello")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random



def jatek():
    jatekosok= ["x", "y"]
    while (input("kezd ela játékot, kilépéhez nomdmeg a q gombot"))!='q':
                x=input("az elő játékos dob , nyomdmeg az x gombot")
                while x!=jatekosok[0]:
                    print("rossz gombot nyomtál meg!")
                    x=input("az elő játékos dob , nyomdmeg az x gombot")
                szam1=random.randint(1,6)
                y=input("az elő játékos dob , nyomdmeg az y gombot")
                while y!=jatekosok[1]:
                    print("rossz gombot nyomtál meg!")
                    y=input("az elő játékos dob , nyomdmeg az y gombot")
                szam2=random.randint(1,6)
                print("az elso szam az %d \na második szám: %d " %(szam1, szam2))
                if szam1 > szam2: 
                    print("az első játékos ni
                    yert")
                elif szam2 > szam1:
                    print("a második játékos nyert")
                else:
                    print("döntetlen")

jatek()

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def legfiatalabb(adatok):
    legfiatalabb = min(adatok[1])
    return adatok[1].index(legfiatalabb)

def legidosebb(adatok):
    legidosebb = max(adatok[1])
    return adatok[1].index(legidosebb)


adatok=[[] , []]
kilep = 'q'
bemenet= input("szeretnél adatokat megadni?  i/n")
while bemenet == "i":
    nev = input("add meg a teljes neved")
    adatok[0].append(nev)
    szulev = int(input("add meg a születési éved"))
    adatok[1].append(szulev)
    bemenet = input("szeretnél adatokat megadni?  i/n")

legfiatalabb = adatok[0][legfiatalabb(adatok)]
legidosebb = adatok[0][legidosebb(adatok)]

print("a legidosebb személy %s" %legidosebb)
print("a legfiatalabb személy %s" %legfiatalabb)

#---------------------------------------------------------------------------------------------------------------------------------------------
#webcimek=[]
#cim = input("adj meg egy webcímet! ")
#webcimek.append(cim)
#print(webcimek)


def legtobb(lista):
    temp=[]
    count=[]
    for i in lista:
        i.split('.')
        temp.append(i)
    for i in range(len(temp)):
        for j in range(len(temp)):
            count.append()
weblap=[]
be=input("adj meg egy címet")
while be!='\n':
    weblap.append(be)
    be=input("adj meg egy webcímet")

'''
#---------------------------------------------------------------------------------------------------------------------------------------------------
'''
def osszeadas(a,b):
    return a + b

szamok = osszeadas(3, 2)
print(szamok)

'''
#----------------első fldat -----------------------------------------------------------------------------------------------------------------
from math import sqrt


szam1 = int(input("adj meg egy számot"))
szam2 = int(input("adj meg még eg számot"))

if szam1 < szam2 :
    print("a második szám a nagyobb")
elif szam1 > szam2 :
    print("az első szám a nagyobb")
else: 
    print("a két szám egyenlő") 
#----------------második feladat---------------------------------------------------------------------------------------------------------------------------------
oldal1 = int(input("add meg az első oldalt"))
oldal2 = int(input("add meg a második oldalt"))
oldal3 = int(input("add meg a harmadik oldalt"))

if oldal1 + oldal2 > oldal3:
    print("a háromszög megszerkeszthető")
elif oldal1 + oldal3 > oldal2:
    print("a háromszög megszerkeszthető")
elif oldal2 + oldal3 > oldal1:
    print("a háromszög megszerkeszthető")
else:
    print("a háromszög nem szerkeszthető!")
#---------------harmadik feladat---------------------------------------------------------------------------------------------------------------------------------------
a = int(input("add meg az első oldalt"))
b = int(input("add meg a második oldalt"))
c = int(input("add meg a harmadik oldalt"))

kerulet = a+b+c 
print(kerulet)

s= kerulet/2
terulet= sqrt(s* (s-a) * (s-b) * (s-c))
print(terulet)
#-----------------------------------------------------------------------------------------------------------
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

'''
ujlista.sort() #kulombozo tipusokat nem tud sortolni
print(ujlista)
'''
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



'''
adatlopas=[]
while len(adatlopas)<29:
    adatlopas.append(str(input("Adja meg a teljes nevét!")))
    adatlopas.append(str(input("Adja meg a szül. helyét!")))
    adatlopas.append(str(input("Adja meg az anyja nevét! ")))

adatlopas.sort()
print(adatlopas)
'''
'''''
adatok=[]
for i in range(5):
    adatok.append(str(input("név: "))+","+str(input("szül. hely: "))+", "+str(input("anja neve: ")))

adatok.sort()
print(adatok)
'''''
szamlista=[]
for i in range(10):
    szamlista.append(input("adj meg egy elemet:"))

ujlista=[x for x in szamlista if type(x)==int]
print(ujlista)
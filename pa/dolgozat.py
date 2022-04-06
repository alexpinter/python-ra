#feladat

#Írj programot, amely bekér a bementről két számot. Hozz létre egy listát, amelyet feltöltesz számokkal.
#  Az első beolvasott szám mondja meg, hogy hány eleme legyen a listának 1-n-ig, a második szám pedig a hatvány kitevő lesz. 
#Pl.: 
#Első szám: n=5; 
#Második szám: m=4, 
#akkor az eredmény ezt adja: [1**4, 2**4, 3**4, 4**4, 5**4]
#feladat

#Olvass be a billentyűzetről egy max 20 karakter hosszú mondatot, 
# amely csak az angol ABC betűit tartalmazhatja. Végezd el a szükséges input ellenőrzést, majd a beolvasott mondatot előbb fordítsd meg, és utána változtasd mindegyik második betűjét nagybetűvé!

#feladat

#Olvass be a billentyűzetről egy max 20 karakter hosszú szöveget, amely csak az angol ABC betűit tartalmazhatja, 
# majd számold meg, hogy az egyes betűkből hány darab érkezett. Ha valamely betű nem jelenik meg 
# a szövegben, akkor azt ne írd ki, csak azokat amelyek megjelennek. Végezd el a szükséges input ellenőrzést is!

#-------------------------------------------------1 feladat-----------------------------------------------------------------------------------------------------------------


lista = []
n=  int(input("adj meg 1 szamot"))
m=  int(input("adj meg 1 szamot"))
for i in range (1, n+1):
    lista.append(i**n)


print(lista)

#------------------------------------------------2 feladat----------------------------------------------------------------------------------------------------------------------
szoveg2 = []
mondat = str(input("adj meg egy 20 karakterből álló mondatot")) [::-1]

while not len(mondat) == 20 and mondat.isalpha() :
    mondat = str(input("nem elég/több a karakter! Adj meg egy 20 karakterből álló mondatot")) [::-1]


for i in range (len(mondat)):
    if  not i%2:
        szoveg2.append(mondat[i])
    else:    
        szoveg2.append(mondat[i].upper())
mondat = "".join(szoveg2)


print(mondat)
#--------------------------------------------3 feladat--------------------------------------------------------------------------------------------------------------------
eredmeny = []
szamlalo = ['q', 'w', 'e' , 'r','t','z' ,'u', 'i', 'o','p','a','s','d','f','g','h','j','k','l','y','x','c','v','b','n','m']
szoveg = str(input("adj meg egy 20 karakterből álló szöveget")) 
q = 0
w = 0
e =0
r =0
t =0
z =0
u =0
i =0
o =0
p =0
a =0
s =0
f =0
h =0
j =0
k =0
l =0
y =0
x =0
c =0
v =0
b =0
n =0
m =0

while not len(szoveg) == 20 and szoveg.isalpha() :
    szoveg = str(input("nem 20 karakter! Adj meg egy 20 karakterből álló szöveget!")) 
#for i in szoveg:
#    if szoveg[i] in szamlalo:
#        eredmeny.append("ok")

if q and w and r and t and z and u and i and o and p and a and s and d and f and g and  h  and j and k and l and y and x and c and v and b and n and m in szoveg:
    +1

print(q and w and r and t and z and u and i and o and p and a and s and d and f and g and  h  and j and k and l and y and x and c and v and b and n and m)


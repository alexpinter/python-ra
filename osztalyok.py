
# osztalyok , es objektumok
# a pythonban szinte minden objektum, tulajdonságokkal és metódusokkal együtt.
# osztalyt letrehozni class kulcsszoval lehet



class en_osztalyom:
    x = 5
osztaly = en_osztalyom()
print(osztaly.x)

# hogy jobban megértsük az osztályokat, meg kell előbb érteni az __init__() függvényt
# minden osztálynak van egy __init__() nvű függvénye, amely minden alkalommal lefut amikor az osztályt inicializáljuk.
# hogy megértsük hozzunk létre egy Szemely osztalyt és használjuk az __init__() függvényt, hogy  értékeket rendeljünk a névhez és a korhoz.


# az init függvény automatikusanb meghívódik mindn egyes alkalommal amikor használjuk az osztályt egy új objektum létrehozására.
# A self paraméter a pillanatnyi osztály állapotára hivatkozik és ezzel tudjuk elérni az osztályhoz tartozó változókat.
# nem kötelező self-nek nevezni , elnevezhetjük bárminek, de az osztályon belüli függvényk első paramétere kell, hogy legyen.
# Nézzünk egy újabb példát erre:
class Szemely:
    def __init__(osztaly_neve, nev, eletkor):
        osztaly_neve.nev=nev
        osztaly_neve.eletkor=eletkor

    def az_en_nevem(ez_lehet_barmi):
        print("az én nevem " + str(ez_lehet_barmi.nev))

    def az_en_korom(megint_lehet_barmi_a_neve):
        print("az én kororm " + str(megint_lehet_barmi_a_neve.eletkor))    


szemely1=Szemely("pista",21)
szemely1.az_en_nevem()
szemely1.az_en_korom()
#meg is tudom változtatni az objektum valamelyik értékét
szemely1.eletkor=34
szemely1.az_en_korom()
#törölni is tudunk objektum tulajdonsagokt, vagy egész objektumot is
#del szemely1.eletkor
#szemely1.az_en_korom()
#del szemely1
#szemely1.az_en_nevem()
f =  open("C:\\Users\\szakinf\\Documents\\pa\\autook.csv", "a")
class autok:
    def __init__(self, marka ,modell ,tipus,tankmeret,uzemanyagszint):
        self.marka = marka
        self.modell= modell
        self.tipus= tipus
        self.tankmeret = tankmeret
        self.uzemanyagszint=uzemanyagszint
    def tulajdonságok(self):
        print(f"az autó teljes típusa: {self.marka, self.modell,self.tipus}")

    def uzemanyag_szazalek(self):
        uzemanyagszint = float(self.uzemanyagszint) / float(self.tankmeret) * 100
        print(f"az üzemanyagszint pillanatnyilag: {uzemanyagszint}%")
        if uzemanyagszint < 10:
            print(f"az uzemanyagszint 10% alá csökkent! Tankoljon!!")
    def fajliras(self):
        f.write(f"{self.marka};{self.modell};{self.tipus};{self.tankmeret};{self.uzemanyagszint}\n")
        
        

         
        
f.close()
auto1 = autok(input("add meg az autó márkáját"), input("add meg az autó modelljét"), input("add meg az autó típusát"), input("add meg az autó tankméretét"),  input("add meg az üzemanyagszintjét"))
auto2 = autok(input("add meg az autó márkáját"), input("add meg az autó modelljét"), input("add meg az autó típusát"), input("add meg az autó tankméretét"),  input("add meg az üzemanyagszintjét"))
auto3 = autok(input("add meg az autó márkáját"), input("add meg az autó modelljét"), input("add meg az autó típusát"), input("add meg az autó tankméretét"),  input("add meg az üzemanyagszintjét"))
auto1.uzemanyag_szazalek()
auto1.tulajdonságok()
auto2.uzemanyag_szazalek()
auto2.tulajdonságok()
auto3.uzemanyag_szazalek()
auto3.tulajdonságok()
auto1.fajliras()
auto2.fajliras()
auto3.fajliras()





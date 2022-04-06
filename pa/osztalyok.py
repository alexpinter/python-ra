class en_osztalyom:
    x = 5
osztaly = en_osztalyom()
print(osztaly.x)

#hogy jpbban megértsük az osztályokat, meg kell előbb érteni az __init__() függvényt
#minden osztálynak van egy __init__() nvű függvénye, amely minden alkalommal lefut amikor az osztályt inicializáljuk.
 #hogy megértsük hozzunk létre egy Szemely osztalyt és használjuk az __init__()



class Szemely:
    def __init__(self, name, age):
        self.name=name
        self.age=age

szemely1=Szemely("pista",21)

print(szemely1.name)
print(szemely1.age)
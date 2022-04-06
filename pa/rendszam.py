rendszam = ["JKL123", "ABC987" , "QWE613", "RTZ654"]
tabla = input("add meg a rendszamot")

while  not (len(tabla)==6 and tabla[:3].isupper() and tabla[3:].isnumeric()):
    tabla = input("add meg a rendszamot")
if tabla in rendszam:
    print("a vezeto jogosult a belépésre")
else:
    print("húzz innen")


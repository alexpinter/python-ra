'''
lista = [i**3 for i in range (1, int(input("adj meg egy számot")))]
print(lista)
'''
from lib2to3.pgen2.pgen import DFAState
from this import d


szoveg2 = []
valtozo = str(input("adj meg egy 10 karakter hosszu szoveget"))
while len(valtozo) >= 10 and valtozo.isalpha() :
   valtozo =  str(input(" a szoveg tul hosszu!adj meg egy max10 karakter hosszu szoveget"))
for i in range (len(valtozo)):
    if  not i%2:
        szoveg2.append(valtozo[i])
    else:    
        szoveg2.append(valtozo[i].upper())
valtozo = "".join(szoveg2)
print(valtozo)

'''''
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
'''

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


'''''
for x in lista[3]:
    lista[3].sort()
         
        print("születési éve: %d" %lista[3][i])
'''

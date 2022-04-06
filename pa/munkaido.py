f =  open("C:\\Users\\szakinf\\Documents\\pa\\nyilvantartas.csv", "w", encoding="utf-8")

munkaidony = {
    "hetfo" : [0,0,0],
    "kedd" : [0,0,0],
    "szerda" : [0,0,0],
    "Csütörtök" : [0,0,0],
    "péntek" : [0,0,0]

}

for i in munkaidony:
    munkaidony[i][0] = int(input("Mikor kezdődött a munkaaideje")) 
    munkaidony[i][1] = int(input("Mikor végez")) 
    munkaidony[i][2] = munkaidony[i][1]-munkaidony[i][0]


print(munkaidony)
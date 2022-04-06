

def ellenoriz(bemenet):
    while (not(len(bemenet)==6 and bemenet.isdigit())):
        print("a kod hosszusaga vgy karakterei nem megfelelok")
        return False
    return True 
    

def helyese (bemenet):
    osszeg=0
    for i in range(len(bemenet)-1):
        osszeg=osszeg+int(bemenet[i])
        maradek=osszeg%6
    while maradek!=int(bemenet[-1]):
        print("a kód nem felel m egg a második kritériumnak")
        return False
    return True

kodok=[]
bemenet = (input("adj meg egy 6 számjegyű termék kódot"))
while bemenet!='q':
    while (not(ellenoriz(bemenet) and helyese(bemenet))):
        bemenet=input("add meg úlyra a termékkódot helyesen: ")
    kodok.append(bemenet)
    bemenet=(input("add meg a termékkódot"))
print("kilép!")
print(kodok)


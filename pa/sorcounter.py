def szamlalo():
    f =  open("C:\\Users\\szakinf\\Documents\\pa\\ebetu.txt", "r", encoding="utf-8")


    sorok= f.readlines()
    sor=0
    for i in sorok:
        sor+=1
        i = i.replace('\n', '')
        if i[-1] == 'i':
            print("Az alábbi sorok végen van i betű " +str(sor))

    f.close()
szamlalo()






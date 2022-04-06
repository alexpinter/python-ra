tomb=[]
Itomb=[]

for i in range(10):
    inpuut=(input("Add meg a következő értéket:"))
    try:
        if (float(inpuut)%1!=0):
            tomb.append(float(inpuut))
        elif (int(inpuut)%1==0):
            tomb.append(int(inpuut))
            Itomb.append(int(inpuut))
    except:
            tomb.append(str(inpuut))
print(Itomb)








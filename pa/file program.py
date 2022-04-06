#1493
sorok = []
sorok2  = []
f = open("C:\\Users\\szakinf\\Documents\\pa\\energia.csv" , "r" ).readlines()

for i in range(len(f)):
    if i > 0:
        sorok.append(f[i].split(";")[0])

for i in range(len(f)):
    if i > 0:
        sorok2.append(f[i].split(";")[2])




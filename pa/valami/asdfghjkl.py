f=open("C:\\Users\\szakinf\\Documents\\pa\\valami\\auto.txt", 'r', encoding="utf-8")

def tordel(f):
    bekezdesek=f.readlines()
    for bekezdes in bekezdesek:
        bekezdes=bekezdes.replace("\n", "")
        mondatok=bekezdes.split(".")
        ujbekezdesek.append(mondatok)
    return ujbelkezdesek

"def kiir(tartalom):"
f.close()

def gyenge_jelszavak(lista):
    jelsz1 = list()
    jelsz2 = list() #számosra gyenge
    jelsz3 = list() # 5re gyenge
    jelsz4 = list() # 3. feltétel
    vegso = list()

    for s in lista:
        jelsz2.append(s)

    szam = list()
    for a in range(10):
        szam.append(a)
        for b in range(len(szam)):
            szam[b] = str(b)

    for i in lista:
        for c in i:
            for g in szam:
                if g == c:
                    jelsz1.append(i)

    aa = list()
    for bb in jelsz4:
        aa.append(bb)
        for cc in jelsz4:
            for dd in aa:
                while cc == dd:
                    szka = -1
                    for ee in jelsz4:
                        szka += 1
                        hely1 = list()
                        for ff in range(len(jelsz4)):
                            hely1.append(ff)
                        hely1.remove(hely1[szka])
                        for gg in hely1:
                            if ee == jelsz4[gg]:
                                jelsz4.remove(str(jelsz4[gg]))
                                break
                        hely1.clear()

    for e in jelsz1:
        for z in jelsz2:
            if z == e:
                jelsz2.remove(z)

    for x in lista:
        hossz = 0
        for y in x:
            hossz += 1
        if hossz < 5:
            jelsz3.append(x)

    szo = list()
    lii = "valami"
    for n in lista:
        lii = n
        for m in lii:
            szo.append(m)
            for t in range(len(szo) - 1):
                if t >= len(szo) - 1:
                    break
                if t >= len(szo) - 2:
                    break
                if szo[t] == "1":
                    if szo[t + 1] == "2":
                        if szo[t + 2] == "3":
                            jelsz4.append(n)

            for t in range(len(szo) - 1):
                if t >= len(szo) - 1:
                    break
                if t >= len(szo) - 2:
                    break
                if t >= len(szo) - 3:
                    break
                if t >= len(szo) - 4:
                    break
                if t >= len(szo) - 5:
                    break
                if szo[t] == "J" or szo[t] == "j":
                    if szo[t + 1] == "E" or szo[t + 1] == "e":
                        if szo[t + 2] == "L" or szo[t + 2] == "l":
                            if szo[t + 3] == "S" or szo[t + 3] == "s":
                                if szo[t + 4] == "Z" or szo[t + 4] == "z":
                                    if szo[t + 5] == "o":
                                        jelsz4.append(n)
                                    elif szo[t + 5] == "O":
                                        jelsz4.append(n)

        szo.clear()

    vg = list()
    for lk in jelsz4:
        vg.append(lk)
        for zz in jelsz4:
            for pk in vg:
                while zz == pk:
                    szkk = -1
                    for ww in jelsz4:
                        szkk += 1
                        hely2 = list()
                        for zz in range(len(jelsz4)):
                            hely2.append(zz)
                        hely2.remove(hely2[szkk])
                        for xx in hely2:
                            if ww == jelsz4[xx]:
                                jelsz4.remove(str(jelsz4[xx]))
                                break
                        hely2.clear()

    for pp in jelsz2:
        vegso.append(pp)
    for cc in jelsz3:
        vegso.append(cc)
    for dd in jelsz4:
        vegso.append(dd)

    szkd=-1
    for kk in vegso:
        szkd+=1
        hely3 = list()
        for ff in range(len(vegso)):
            hely3.append(ff)
        hely3.remove(hely3[szkd])
        for nn in hely3:
            if kk == vegso[nn]:
                vegso.remove(str(vegso[nn]))
                break
        hely3.clear()

    soo = list()
    aaa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for s1 in aaa:
        soo.append(s1)

    hhh = list()
    for fff in range(len(aaa)):
        hhh.append(fff)
    hhhh4 = -1
    for ppp in vegso:
        hhhh4 += 1
        for nnn in hhh:
            if ppp == vegso[nnn]:
                vegso.insert(hhhh4 + 1, vegso.pop(nnn))
                break

    return vegso

jelsz = ['Root', 'Kekw2000', 'H0sszuJelszoG0esBrrr', 'Admin123456', 'sub2Pewdiepie', 'asdqwe', 'K1L0']
print(gyenge_jelszavak(jelsz))
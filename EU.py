# 2. feladat

class EUcsatl:
    def __init__(self, line):
        darabol = line.split(";")
        self.orszag = darabol[0]
        self.datum = (darabol[1].rstrip("\n"))

EUorszagok = []
with open("EUcsatlakozas.txt", "rt", encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        EUorszagok.append(EUcsatl(lines[i]))

# 3. feladat
print("3. feladat: EU tagállaminak száma: {} db".format(len(EUorszagok)))

# 4. feladat
csatl_2007 = 0
for i in range(0, len(EUorszagok)):
    if '2007' in EUorszagok[i].datum:
        csatl_2007 += 1
print("4. feladat: 2007-ben {} ország csatlkozott.".format(csatl_2007))

# 5. Feladat
for i in range(0, len(EUorszagok)):
    if EUorszagok[i].orszag == 'Magyarország':
        print("5. feladat: Magyarország csatlakozásánka  dátuma: {}".format(EUorszagok[i].datum))
        break

# 6. feladat májusbn volt-e csatlak
for i in range(0, len(EUorszagok)):
    if EUorszagok[i].datum[5:7] == '05':
        print("6. feladat: Májusban volt csatlakozás")
        break

# 7. feladat: utoljára csatlakozott állam - Ezt nem tudtam máshogy, túlkomplikáltam...
utolsoev = 0
utolsoho = 0
utolsonap = 0
for i in range(0, len(EUorszagok)):
    if int(EUorszagok[i].datum[:4]) > utolsoev:
        utolsoev = int(EUorszagok[i].datum[:4])
for j in range(0, len(EUorszagok)):
    if int(EUorszagok[j].datum[:4]) == utolsoev:
        if int(EUorszagok[j].datum[5:7]) > utolsoho:
           utolsoho = int(EUorszagok[j].datum[5:7])
for i in range(0, len(EUorszagok)):
    if int(EUorszagok[i].datum[:4])==utolsoev:
        if int(EUorszagok[i].datum[5:7]) == utolsoho:
            if int(EUorszagok[i].datum[8:10]) > utolsonap:
                utolsonap = int(EUorszagok[i].datum[8:10])

for i in range(0, len(EUorszagok)):
    if utolsoev == int(EUorszagok[i].datum[:4]) and utolsoho == int(EUorszagok[i].datum[5:7]) and utolsonap == int(EUorszagok[i].datum[8:10]):
        print("7. feladat: Legutoljára csatlakozott ország: {}".format(EUorszagok[i].orszag))

#8. feladat - statisztika
csatléve = []
for i in range(0, len(EUorszagok)):
    if (EUorszagok[i].datum[:4]) not in csatléve:
        csatléve.append((EUorszagok[i].datum[:4]))

darab = []
for i in range(0, len(csatléve)):
    db=0
    for j in range(len(EUorszagok)):
        if csatléve[i] == (EUorszagok[j].datum[:4]):
            db += 1
    darab.append(db)
print("8. feladat: Statisztika")
for i in range(len(csatléve)):
    print("\t \t{} - {} ország".format(csatléve[i], darab[i]))

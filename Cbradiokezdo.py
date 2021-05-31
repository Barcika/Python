# 2. Feladat - datbeolvasás, osztály létrehozás

class Sofor:
    def __init__(self, line): # feldaraboljuk a soron belüli infót
        darabol = line.split(";") #;-vel elválaszt
        self.ora = int(darabol[0]) # egész szám
        self.percertek = int(darabol[1]) # egész szám
        self.adasszam = int(darabol[2]) # egész szám
        self.becenev = darabol[3].rstrip("\n") # string

soforok = []
with open("cb.txt", "rt", encoding="utf-8") as nevsor: # elkezdem a beolvasást, az UTF nem kötelező
   lines = nevsor.readlines() #sorok olvasása
   for i in range(1, len(lines)): # azért 1-től, mert így a fejlécet kihagyja
       soforok.append(Sofor(lines[i])) # elhelyeztük a listába a sofőröket

# 3. Feladat - Bejegyzések számánk meghatározása és kiiratása

print("3. Feladat: Bejegyzések száma: {} db".format(len(soforok))) # len-l megszámolhatom a darbszámot,  lista hosszát

# 4. Feladat - 1 percen belül volt-e 4 hívásindítás

k = 0
while k < len(soforok) and soforok[k].adasszam != 4: #amíg kisebb a k mint a sofőrlista hossza és nem talál adásszám egyezést, addig megy a ciklus
    k += 1
indadas = k < len(soforok) # ez utóbbi vagy igaz vagy hamis, k vagy kisebb vagy nem, így lesz logikai változó
if indadas:
    print("4. Feladat: Volt 4 adást indító sofőr")

# 5. Feladat - Megadott sofőr nevét ellenőrizni, összesen hány hívása volt
soforNev = input("5. Feladat: Kérek egy nevet: ") # egy sofőr többször is van, végig kell mennem a listán!!!
radiohaszn = 0
for sofor in soforok:
    if sofor.becenev == soforNev:
        radiohaszn += sofor.adasszam
if radiohaszn > 0:
    print("\t"*2, "{} {}x használta a CB rádiót.".format(soforNev, radiohaszn)) # 2 tabbal teszi beljebb
else:
    print("\t"*2, "Nincs ilyen nevű sofőr!")

# 6. Feladat - ÁtszámolPercre fg készítése
def AtszamolPercre(ora, perc): # függvényt hozunk létre óra, perc, másodperc paraméterekkel
    return ora * 60 + perc

# 7. feladat - szöveges állomány készítése cb2.txt néven
with open("cb2.txt", "wt", encoding="utf-8") as ujallomany:
    ujallomany.write("Kezdes; Nev; AdasDb \n")
    for sofor in soforok:
        ujallomany.write("{};{};{} \n".format(
            AtszamolPercre(sofor.ora, sofor.percertek),
            sofor.becenev,
            sofor.adasszam
        ))

# 8. feladat - sofőrök száma

soforlist = []

for sofor in range(1, len(soforok)):
   if soforok[sofor].becenev not in soforlist:
        soforlist.append(soforok[sofor].becenev)

print("8. feladat: Sofőrök száma: ", len(soforlist), "fő")

# 9. feladat
print("9. feladat: Legtöbb adást indító sofőr")
adas_nevenkent = []
for sofor in range(0, len(soforlist)):
    osszhivas = 0
    for i in range(len(soforok)):
        if soforlist[sofor] == soforok[i].becenev:
            osszhivas += soforok[i].adasszam
    adas_nevenkent.append(osszhivas)

for j in range(0, len(adas_nevenkent)):
    if adas_nevenkent[j] == max(adas_nevenkent):
        print("\t"*2, "Név: ", soforlist[j])
        print("\t"*2, "Adások szám: ", max(adas_nevenkent), " alkalom")

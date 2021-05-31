# 1.-2. feladat  BarkaiGábor_Balkezesek.py létrehozása, + adatok beolvasása és tárolása

class Jatekos:
    def __init__(self, balkez ):
        darabol = balkez.split(";")
        self.nev = darabol[0]
        self.elso = darabol[1]
        self.utolso = darabol[2]
        self.suly = int(darabol[3])
        self.magassag = int(darabol[4].rstrip("\n"))

jatekosok = []
with open("balkezesek.txt", "rt", encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(1, len(lines)):
        jatekosok.append(Jatekos(lines[i]))

# 3. feladat - hány adatsor van
print("3. feladat: {}".format(len(jatekosok)))

# 4. feladat - 1999 októberében utoljára pályára lépett játékosok neve és testmagassága

print("4. feladat: ")
for i in range(1, len(jatekosok)):
    if jatekosok[i].utolso[:7] == '1999-10':
        print("\t{} {:.1f}".format(jatekosok[i].nev, jatekosok[i].magassag*2.54))

# 5. feladat - évszámbekérés
print("5.feladat: ")
evszam = int(input("Kérek egy 1990 és 1999 közötti évszámot: "))
while evszam < 1990 or evszam > 1999:
    evszam = int(input("Hibás adat! Adja meg helyesen, 1990 és 1999 között: "))

# 6. feladat - a megadott évben pályára lépő játékokosok átlagsúlya
#súlyok = [ sor.suly for sor in jatekosok if (sor.elso[:4] <= evszam <= sor.utolso[:4]) ]
osszsuly = []
for i in range(0, len(jatekosok)):
    if (int(jatekosok[i].elso[:4]) <= evszam <= int(jatekosok[i].utolso[:4])):
        osszsuly.append(jatekosok[i].suly)
print("6. feladat: {:.2f}".format(sum(osszsuly) / len(osszsuly)))


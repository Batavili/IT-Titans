import os,random
os.system("cls")

class Suti:
    def __init__(self, nev, tipus, ar, egyseg):
        self.nev = nev
        self.tipus = tipus
        self.ar = ar
        self.egyseg = egyseg
        self.eladas = 0
        self.bevetel = 0

    def EladasGeneralas(self):
        return random.randint(100, 500)

    def BevetelSzamitas(self):
        self.bevetel = self.eladas * self.ar  

sutemenyek = []
with open("13_2024-03-10_11-16-56_4255.txt", "r", encoding="utf-8") as szoveg:
    for sor in szoveg:
        sor = sor.strip()
        if sor == "":
            continue

        nev, tipus, ar, egyseg = sor.split(";")
        ar = int(ar)

        suti = Suti(nev, tipus, ar, egyseg)
        suti.eladas = suti.EladasGeneralas()
        suti.BevetelSzamitas()

        sutemenyek.append(suti)

with open("sutik.txt", "w", encoding="utf-8") as szoveg:
    for suti in sutemenyek:
        szoveg.write(f"Sütemény neve: {suti.nev}\n")
        szoveg.write(f"A sütemény kiszerelése: {suti.egyseg}\n")
        szoveg.write(f"Eladott mennyiség: {suti.eladas} {suti.egyseg}\n")
        szoveg.write(f"Bevétel: {suti.bevetel} Ft\n")

        if suti.bevetel>100000:
            szoveg.write("NÉPSZERŰ\n")
        szoveg.write("-------------------------------------\n")

        #iderakom kommentbe hogy majd késöbb könnyü legyen a ppt be berakni a vélemény részhez a feladatoknál de valószinüleg rövidebb lesz ott mint itt: A Fagyi3 feladat az elején még lassan ment de utána belelendültem, új dolog volt nekem hogy kellet self lokális változót használni mert ugye nem jegyezné meg a def-en kivul anelkul csak eddig nem csinaltam ilyet. A class is uj dolog volt nekem de az csak annyi hogy osztályba rakom szóval arra könnyen rájöttem, A konstruktort pedig nagyjából megértettem. Összegzésben egész kis mókás feladat volt,tanultam belőle egy-kettőt -Bata Vilmos"
        #UI: nalam valamiért utf-8 karakterkódolással és cp1250 vel se müködik a magyar ékezet ami nemtudom miert van
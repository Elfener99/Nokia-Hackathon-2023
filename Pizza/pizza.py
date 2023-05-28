#!/usr/bin/env python3
class Termek():
    def __init__(self, nev ,ar):
        self.nev = nev
        self.ar = ar
def rendeles(bemenet):
    global kosar
    if "sonkás" in bemenet and "kukoricás" in bemenet:
        meret, szorzo = meretek(bemenet)
        while meret == "":
            print("Eladó: Milyen méretű sonkás-kukoricás pizzát szeretnél?")
            meret, szorzo = meretek(input("Felhasználó: ").lower())
        extra = extrafeltetek()
        if extra == None:
            kosar.append(Termek(f"{meret} sonkás-kukoricás pizza",3050 * szorzo))
        else:
            kosar.append(Termek(f"{meret} sonkás-kukoricás pizza +{' +'.join(extra)}",3050 * szorzo + len(extra) * 100))
    elif "sonkás" in bemenet:
        meret, szorzo = meretek(bemenet)
        while meret == "":
            print("Eladó: Milyen méretű sonkás pizzát szeretnél?")
            meret, szorzo = meretek(input("Felhasználó: ").lower())
        extra = extrafeltetek()
        if extra == None:
            kosar.append(Termek(f"{meret} sonkás pizza",3000 * szorzo))
        else:
            kosar.append(Termek(f"{meret} sonkás pizza +{' +'.join(extra)}",3000 * szorzo + len(extra) * 100))
    elif "szalámi" in bemenet:
        meret, szorzo = meretek(bemenet)
        while meret == "":
            print("Eladó: Milyen méretű szalámis pizzát szeretnél?")
            meret, szorzo = meretek(input("Felhasználó: ").lower())
        extra = extrafeltetek()
        if extra == None:
            kosar.append(Termek(f"{meret} szalámis pizza",3000 * szorzo))
        else:
            kosar.append(Termek(f"{meret} szalámis pizza +{' +'.join(extra)}",3000 * szorzo + len(extra) * 100))
    elif "víz" in bemenet or "viz" in bemenet:
        kosar.append(Termek("ásványvíz",500))
    elif "narancs" in bemenet:
        kosar.append(Termek("narancslé",600))
    elif "limonádé" in bemenet:
        kosar.append(Termek("limonádé",900))
    elif "pizza" in bemenet:
        print("Eladó: Milyen pizzát?")
    elif "menü" in bemenet or "mi" in bemenet:
        print("Eladó: Pizzák: sonkás, sonkás-kukoricás, szalámis\nEladó: Extra feltétek: kukorica, szalámi, erdei gomba, sonka\nEladó: Italok: ásványvíz, narancslé, limonádé\nEladó: A pizzák 3 méretben elérhetők (kicsi, közepes, nagy).")
    else:
        print("Eladó: Elnézést, ezt nem értettem.")
def extrafeltetek():
        print("Eladó: Szeretnél rá extra feltétet? Ha igen, mit?")
        extrafeltet = input("Felhasználó: ").lower()
        extra = []
        if "nem" in extrafeltet:
            return None
        else:
            if "kukoric" not in extrafeltet and "szalámi" not in extrafeltet and "gomb" not in extrafeltet and "sonk" not in extrafeltet:
                return extrafeltetek()
            if "kukoric" in extrafeltet:
                extra.append("kukorica")
            if "szalámi" in extrafeltet:
                extra.append("szalámi")
            if "gomb" in extrafeltet:
                extra.append("erdeigomba")
            if "sonk" in extrafeltet:
                extra.append("sonka")
        return extra
def meretek(bemenet):
    if "nagy" in bemenet:
        meret = "nagy"
        szorzo = 1.5
    elif "közepes" in bemenet:
        meret = "közepes"
        szorzo = 1.2
    elif "kicsi" in bemenet or "kis" in bemenet:
        meret = "kicsi"
        szorzo = 1.0
    else:
        meret = ""
        szorzo = 1.0
    return meret, szorzo
def kosarformat(kosar):
    rendeles = {}
    for item in kosar:
        if item.nev not in rendeles.keys():
            rendeles[item.nev] = 0
        rendeles[item.nev] += 1
    lista = []
    for item in rendeles:
        db = ""
        if rendeles[item] == 1:
            db = "egy"
        else:
            db = str(rendeles[item]) + " db"
        lista.append(f"{db} {item}")
    return ', '.join(lista)
def befejez():
    global kosar
    osszeg = 0
    osszegzes = ""
    for item in kosar:
        osszegzes += f"{item.nev}\t{int(item.ar)} Ft\n"
        osszeg += item.ar
    osszegzes += f"Végösszeg\t{int(osszeg)} Ft\n"
    print("\nÖsszegzés (mentve a rendeles.txt fájlba):\n---")
    print(osszegzes,end="")
    print("---")
    with open("rendeles.txt","w",encoding="UTF-8") as file:
        file.write(osszegzes)
kosar = []
print("Eladó: Üdvözöllek a pizzériánkban! Mit szeretnél rendelni?")
rendeles(input("Felhasználó: ").lower())
while True:
    if len(kosar) > 0:
        print(f"Tehát lesz {kosarformat(kosar)}. Szeretnél valami mást is?")
    bemenet = input("Felhasználó: ").lower()
    if "nem" in bemenet or "ennyi" in bemenet:
        befejez()
        break
    else:
        rendeles(bemenet)

import os
os.system("cls")

def fagylaltNevek():
    fagyinevek = []
    while True:
        fagyinev = input("Kérem a fagylalt nevét: ")
        if not fagyinev:
            break
        fagyinevek.append(fagyinev)
    return fagyinevek
    
def Statisztika(fagyinevek):
    fagylaltnevekszama = len(fagyinevek)
    vegandarabszam = 0

    for fagyinev in fagyinevek:
        if "vegán" in fagyinev.lower():
            vegandarabszam += 1

    print(f"{fagylaltnevekszama} féle fagylalt kapható.",)
    print(f"Ebből vegán ízesítésű: {vegandarabszam} db",)
    
fagylaltlista = fagylaltNevek()
Statisztika(fagylaltlista)
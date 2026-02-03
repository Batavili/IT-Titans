import os
os.system("cls")

ar =  int(input("mennyibe kerül egy gombóc fagylalt?:"))
tolcser = int(input("menyibe kerül egy tölcsér?:"))
gomboc = int(input("hány gombócot szeretnél venni?:"))

ossz = ar * gomboc

if gomboc <= 3:
    ossz = ossz + tolcser 

print(f"{gomboc} gombóc fagylalt a tölcsérrel együtt {ossz} ft lesz")







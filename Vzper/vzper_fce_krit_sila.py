# ========
# skript pro vypočet kontroly vzperu dle zadaní
# vstupy: J_min, S, l, typ vzperu, F, E, lambda_m
# vystup: F_kr, lambda_vyp, k, posouzení vzperu podle Eulera
# ========

import numpy as np
def vzper(E,Jmin,S,L,typ_vzperu,F,lambda_m):
    # určení typu vzperu
    match typ_vzperu:
        case 1:
            typ = 2 # jednostraně vetknuty
        case 2:
            typ = 1 # jednostraně kloubová podpora, druhý konec posuvná vazba
        case 3:
            typ = 1/np.sqrt(2) # jednostraně vetknuty, druhý konec kloubová podpora
        case 4:
            typ = 1/2 # oboustranně vetknuty
        case _:
            print("Neznámý typ vzpěru, zadjete číslo 1-4.")

    # vypočet kriticke sily

    l0 = L*typ
    Fkr = (np.pi**2*E*Jmin)/l0**2
    k = Fkr/F # bezpecnost
    # výpočet štíhlosti vzperu
    i = np.sqrt(Jmin/S) # polomer kvadratickeho momentu
    lambda_vyp = l0/i #vypoctena stihlost
        
    if lambda_vyp >= lambda_m:
        print("Vzper je bezpečný dle kriteria štíhlosti.")
    else:
        print("Vzper není bezpečný dle kriteria štíhlosti.")

    return Fkr, lambda_vyp, k, typ




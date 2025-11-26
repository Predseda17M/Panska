# ==========
# fce pro výpočet délky vzpěry z bezpecnosti a zatěžující síly
# vstupy: J_min, S, typ vzperu, F, E, lambda_m, k
# výstup: L
# ==========
import numpy as np
def vzper_delka(E,Jmin,typ_vzperu,F,k):
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

    # výpočet délky vzpěry
    L0 = np.sqrt((np.pi**2*E*Jmin)/(F*k))
    L = L0/typ
    return L
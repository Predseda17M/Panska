# vypocet redukovane delky vzpery
import numpy as np
def reduk_delka(L, typ_vzperu):
    """Výpočet redukované délky vzpěry podle typu uložení.

    Args:
        L (float): skutečná délka vzpěry [mm]
        typ_vzperu (int): typ vzpěry (1-4)

    Returns:
        float: redukovaná délka vzpěry [mm]
    """
    match typ_vzperu:
        case 1:
            typ = 2  # jednostraně vetknuty
        case 2:
            typ = 1  # jednostraně kloubová podpora, druhý konec posuvná vazba
        case 3:
            typ = 1 / np.sqrt(2)  # jednostraně vetknuty, druhý konec kloubová podpora
        case 4:
            typ = 1 / 2  # oboustranně vetknuty
        case _:
            raise ValueError("Neznámý typ vzpěru, zadejte číslo 1-4.")

    L0 = L * typ
    return L0


# ========
# vypocet stihlosti
# ========

def stihlost(L0, S, Jmin):
    """Vypočet štíhlosti vzpěry.

    Args:
        l (float): délka vzpěry [mm]
        i_g (float): poloměr setrvačnosti průřezu [mm]

    Returns:
        float: štíhlost vzpěry
    """
    i = np.sqrt(Jmin / S)
    lambda_vyp = L0 / i
    return lambda_vyp


# vypocet Jmin pro základní průřezy 
# čtverec, kruh, obdélník

def Jmin(typ, rozmery):
    """Výpočet minimálního kvadratického momentu průřezu Jmin.

    Args:
        typ (str): typ průřezu ('kruhovy', 'ctvercovy', 'obdelnikovy')
        rozmery (dict): rozměry průřezu

    Returns:
        float: minimální kvadratický moment průřezu Jmin [mm^4]
    """
    if typ == 'kruhovy':
        prumer = rozmery['prumer']
        Jmin = (np.pi / 64) * prumer**4
    
    elif typ == 'ctvercovy':
        strana = rozmery['strana']
        Jmin = (strana**4) / 12
    
    elif typ == 'obdelnikovy':
        vyska = rozmery['vyska']
        sirka = rozmery['sirka']
        Jmin = (sirka * vyska**3) / 12
    
    else:
        raise ValueError("Neznámý typ průřezu. Zadejte 'kruhovy', 'ctvercovy' nebo 'obdelnikovy'.")
    
    return Jmin 
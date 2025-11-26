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
# vypocet Jmin pro základní průřezy 
# čtverec, kruh, obdélník
import numpy as np

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
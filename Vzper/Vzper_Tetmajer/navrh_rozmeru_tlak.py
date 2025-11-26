import numpy as np

# ==========
#skript umí navrhnout rozměry průřezy podle tlaku a typu průřezu
# vstupy jsou dovolené napětí (MPa), typ průřezu, pomer stran, navrhová síla (N)
# pro typ prurezu se musí zapsat pomer_stran (pro obdélníkový průřez)
# skript pracujes kruhovým, čtvercovým a obdélníkovým průřezem
# skript vrací rozměry průřezu v mm a jeho obsah
# ==========

def navrh_rozmeru_tlak(sigma_dov, typ_prurezu, pomer_stran, F_navrh):
    """Návrh rozměrů průřezu podle dovoleného napětí a typu průřezu.

    Args:
        sigma_dov (float): dovolené napětí [MPa]
        typ_prurezu (str): typ průřezu ('kruhovy', 'ctvercovy', 'obdelnikovy')
        pomer_stran (float): poměr stran pro obdélníkový průřez (výška/sirka)

    Returns:
        dict: navržené rozměry průřezu
    """
    rozmery = {}
    
    if typ_prurezu == 'kruhovy':
        # Návrh průměru kruhového průřezu
        prumer = np.sqrt((4 * F_navrh) / (np.pi * sigma_dov))  # pro plný kruh s plochou 1000 mm2
        rozmery['prumer'] = prumer
        S = (np.pi / 4) * prumer**2
    
    elif typ_prurezu == 'ctvercovy':
        # Návrh strany čtvercového průřezu
        strana = np.sqrt(F_navrh/ sigma_dov)  # pro čtverec s plochou 1000 mm2
        rozmery['strana'] = strana
        S = strana**2
    
    elif typ_prurezu == 'obdelnikovy':
        # Návrh stran obdélníkového průřezu
        sirka = np.sqrt(F_navrh / sigma_dov)  # pro obdélník s plochou 2000 mm2
        vyska = pomer_stran * sirka
        rozmery['vyska'] = vyska
        rozmery['sirka'] = sirka
        S  = vyska * sirka
    
    else:
        raise ValueError("Neznámý typ průřezu. Zadejte 'kruhovy', 'ctvercovy' nebo 'obdelnikovy'.")
    
    return rozmery, S
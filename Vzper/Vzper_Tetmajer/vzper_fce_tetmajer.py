## Výpočet podle Tetmajera pro vzpěr

def vzper_tetmajer(a,b,lambda_vyp):
    """Vstupní proměnné: a, b, lambda (materiálové konstanty a štíhlost vzpěry)
    Výstupní proměnné: sigma_kr (kritické napětí)
    """
    sigma_kr = a-b*lambda_vyp
    return sigma_kr


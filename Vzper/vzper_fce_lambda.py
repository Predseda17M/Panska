# ========
# vypocet stihlosti
# ========
import numpy as np

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
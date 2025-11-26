"""_grafy_
    vykresleni grafu v zavislosti na menici se delce apod. 
    aby videli, co jaka velicina ovlivnuje
    
"""
    
import matplotlib.pyplot as plt
import numpy as np
import vzper_fce_krit_sila as vzper
import Vzper.Vzper_fce_obecne.vzper_fce_delka_tyce as vzper_delka
import Vzper.Vzper_fce_obecne.vzper_fce_lambda as vzper_stihlost
# ==========

delky = np.linspace(1000, 10000, 100)  # delka vzpery od 1m do 10m
J_min = 5.67e4  # minimální kvadratický moment průřezu [mm4]
S = 800     # plocha průřezu [mm2]
typ_vzperu = 4      # typ vzperu (1 pro jednostraně vetknutý, 2 pro oboustranně vetknutý atd.)
F = 25000    # působící síla [N]
E = 2.1e5     # modul pružnosti materiálu [MPa]
lambda_m = 108.0  # mezní štíhlost
# ==========
F_kr_list = []
lambda_vyp_list = []
for L in delky:
    F_kr, lambda_vyp, k1 = vzper.vzper(E, J_min, S, L, typ_vzperu, F, lambda_m)
    F_kr_list.append(F_kr)
    lambda_vyp_list.append(lambda_vyp)
    
# Vykreslení grafu kritické síly vs délky vzpěry
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(delky, F_kr_list, label='Kritická síla $F_{kr}$', color='blue')
plt.title('Kritická síla vs Délka vzpěry')
plt.xlabel('Délka vzpěry L [mm]')
plt.ylabel('Kritická síla $F_{kr}$ [N]')
plt.grid()
plt.legend()
plt.show()

# Vykreslení grafu štíhlosti vs délky vzpěry
plt.subplot(1, 2, 2)
plt.plot(delky, lambda_vyp_list, label='Štíhlost $\lambda_{vyp}$', color='orange')
plt.title('Štíhlost vs Délka vzpěry')
plt.xlabel('Délka vzpěry L [mm]')
plt.ylabel('Štíhlost $\lambda_{vyp}$')
plt.grid()
plt.legend()
plt.show()
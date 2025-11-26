import vzper_fce_tetmajer as vzper_tetmajer
import Vzper_fce_obecne.vzper_fce_lambda as vzper_stihlost
import Vzper_fce_obecne.vzper_fce_Jmin as vzper_Jmin
import Vzper_fce_obecne.vzper_fce_reduk_delka as vzper_redk_delka

# ==========
# vstupy skriptu jsou:
# dovolené napětí sigma_dov (MPa)
# typ průřezu (kruhový, čtvercový, obdélníkový)
# poměr stran (pro obdélníkový průřez)
# navrhová síla F_navrh (N)
# délka vzpěry L (mm)
# materiálové konstanty a, b pro výpočet podle Tetmajera
# typ vzperu (1, 2, 3, 4) 
# ==========
sigma_dov = 210  # MPa
typ_prurezu = 'obdelnikovy'  # 'kruhovy', 'ctvercovy', 'obdelnikovy'
pomer_stran = 2  # poměr stran pro obdélník
F_navrh = 100000  # N
L = 3000  # mm
k = 10 # bezpecnost
a = 355  # materiálová konstanta pro Tetmajera
b = 0.61  # materiálová konstanta pro Tetmajera
typ_vzperu = 3  # typ vzpěry (1, 2, 3, 4)
# ==========

# návrh rozměrů průřezu
rozmery, S = vzper_redk_delka.navrh_rozmeru_tlak(sigma_dov, typ_prurezu, pomer_stran, F_navrh)
print(f"Navržené rozměry průřezu: {rozmery}, Plocha S: {S:.2f} mm²")

# výpočet minimálního kvadratického momentu průřezu Jmin
Jmin = vzper_Jmin.Jmin(typ_prurezu, rozmery)
print(f"Minimální kvadratický moment průřezu Jmin: {Jmin:.2f} mm^4")

# výpočet redukované délky vzpěry
L0 = vzper_redk_delka.reduk_delka(L, typ_vzperu)
print(f"Redukovaná délka vzpěry L0: {L0:.2f} mm")

# výpočet štíhlosti vzpěry
lambda_vyp = vzper_stihlost.stihlost(L0, Jmin, S)
print(f"Vypočtená štíhlost vzpěry λ: {lambda_vyp:.2f}")

# výpočet kritického napětí podle Tetmajera
sigma_kr = vzper_tetmajer.vzper_tetmajer(a, b, lambda_vyp)
print(f"Kritické napětí podle Tetmajera σ_kr: {sigma_kr:.2f} MPa")

# posouzení bezpečnsoti vzpěry
F_kr = sigma_kr * S  # kritická síla
print(f"Kritická síla F_kr: {F_kr:.2f} N")
k_vyp = F_kr / F_navrh  # vypočtená bezpečnost
if k_vyp >= k:
    print("Vzper je bezpečný podle Tetmajera.")
else:
    print("Vzper není bezpečný podle Tetmajera.")
print(f"Vypočtená bezpečnost k: {k_vyp:.2f}")   



import vzper_fce_krit_sila as vzper
import vzper_fce_delka_tyce as vzper_delka
import vzper_fce_lambda as vzper_stihlost

# ==========
# definice proměnných
# ==========
J_min = 47500  # minimální kvadratický moment průřezu [mm4]
S = 900     # plocha průřezu [mm2]
L = 2000        # délka vzperu [mm]
typ_vzperu = 4      # typ vzperu (1 pro jednostraně vetknutý, 2 pro oboustranně vetknutý atd.)
F = 35000    # působící síla [N]
E = 2.1e5     # modul pružnosti materiálu [MPa]
lambda_m = 108.0  # mezní štíhlost
# ==========

# výpočet vzperu
F_kr, lambda_vyp, k1, typ = vzper.vzper(E, J_min, S, L, typ_vzperu, F, lambda_m)
print(f"Kritická síla: {F_kr:.2f} N")
print(f"Vypočtená štíhlost: {lambda_vyp:.2f}")
print(f"Bezpečnost: {k1:.2f}")

# vypočet délky vzpěry pro zadanou bezpečnost a sílu
k2 = k1+1/2*k1
F2 = 45000  # nová zatěžující síla [N]
l2 = vzper_delka.vzper_delka(E, J_min, typ_vzperu, F2, k2)

print(f"Délka vzpěry pro bezpečnost {k2:.2f} je {l2:.2f} mm ")

# vypocet stihlosti s novou delkou
l02 = l2*typ
lambda_vyp2 = vzper_stihlost.stihlost(l02, S, J_min)
print(f"Štíhlost vzpěry s délkou {l2:.2f} mm je {lambda_vyp2:.2f} ")

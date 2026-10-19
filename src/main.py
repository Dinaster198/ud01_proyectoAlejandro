"""
Author : Jose Alejandro Salinas Alves
Date : 2026-10-19
Version: 2.0
"""
#valance is on mays because is a const, beacause it change.
eur = int (input("Ingrese euros:"))
VALANCE= 1.08
dolar= eur * VALANCE
print(f" {dolar:.2f} equivalente a {eur}")

print(f" {round(dolar,2)} equivalente a {eur}")
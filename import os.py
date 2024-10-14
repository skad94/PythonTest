import os
import csv
fichier_csv = os.path.join("C:", "\\", "Utilisateurs\skamta\Téléchargements","client_id.csv")
print("start")
for caractere in fichier_csv:
    print(caractere, end='')
print("\nfin")
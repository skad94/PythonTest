import csv
import os
# Chemin vers le fichier CSV (à remplacer par votre chemin)
fichier_csv = os.path.join("C:", "\\", "Utilisateurs\skamta\Téléchargements","client_id.csv")
# fichier_csv = "C:\Utilisateurs\skamta\Téléchargements\id,client_id.csv"

# Fonction pour calculer la somme des prix totaux
def calculer_somme_prix_totaux(fichier_csv, nombre_lignes):
    """Calcule la somme des prix totaux des premières lignes du fichier CSV.

    Args:
        fichier_csv (str): Chemin vers le fichier CSV.
        nombre_lignes (int): Nombre de lignes à considérer.

    Returns:
        float: Somme des prix totaux.
    """

    somme_totale = 0
    with open(fichier_csv, 'r', newline='') as csvfile:
        lecteur = csv.reader(csvfile)
        # Ignorer l'en-tête si nécessaire
        next(lecteur, None)
        for i, ligne in enumerate(lecteur):
            if i == nombre_lignes:
                break
            try:
                prix_total = float(ligne[4])  # Supposons que le prix total est dans la 5ème colonne
                somme_totale += prix_total
            except ValueError:
                print(f"Erreur lors de la conversion du prix total à la ligne {i+2}")
    return somme_totale

# Calcul de la somme pour les 25 premières lignes
if __name__ == "__main__":

    somme = calculer_somme_prix_totaux(fichier_csv, 25)
    print("La somme des prix totaux des 25 premières lignes est :", somme)
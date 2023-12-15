# Adresse IP de l'imprimante
$adresseIP = "10.114.208.200"

# Nom de l'imprimante réseau
$nomImprimante = "LISIEUX_MULTIMEDIA"

# Créer une nouvelle connexion d'imprimante
Add-Printer -ConnectionName "\\imp-lisieux\LISIEUX_MULTIMEDIA"

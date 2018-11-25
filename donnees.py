#creation dictionnaire qui contiendra les mots
liste_mots = [
    "garage",
    "piscine",
    "pantalon",
    "chemise",
] #on ne s'embête pas à en mettre plus ;)

#initialisation de la varaible qui contiendra les chances
chances_restantes = 8 #8 essais par mot, c'est un compteur

#creation du fichier contenant les scores
liste_scores = "scores"

#string contenant les lettres utilisées, vierge au depart, elle devrait etre reinitialisé lorsque l'IA choisira un mot au hasard,
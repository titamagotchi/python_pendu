from python_pendu.fonctions import *

continuer_partie = "o"

scores = recup_scores()

nom = demande_nom()

if utilisateur not in scores.keys():
    scores[utilisateur] = 0

while continuer_partie == "o" or "O":
    print ("Votre score est de : {0} ").format(scores[utilisateur])
    mot_choisi = choisir_mot_alea()
    lettres_utilisees = []
    mot_a_deviner = mot_cacher()
    nb_chances = chances_restantes
    while nb_chances > 0 and "*" in mot_a_deviner:
        print("Il vous reste {0} chances pour trouver le mot : {1} ".format(nb_chances, mot_a_deviner))
        info_lettres_utilisees()
        lettre = demande_lettre()
        remplace_lettre()
    if "*" not in mot_a_deviner:
        print("Bravo! Vous avez trouvé!Il s'agissait bien de {0}".format(mot_a_deviner))
        scores[utilisateur]+=nb_chances
    else:
        print("Perdu! Vous perdez tout vos points!")
        scores[utilisateur]==0
    continuer_partie = input("Souhaitez vous continuer? (o/n)")
    save_scores(scores)



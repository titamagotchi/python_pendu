import os
import pickle
import random
from python_pendu.donnees import *
#on commence par importer les modules et le fichier donnees

def demande_nom():
    nom_utilisateur = input("Veuillez saisir votre nom:")
    nom_utilisateur = nom_utilisateur[0].upper() + nom_utilisateur[1:].lower()
    return nom_utilisateur

#fonction qui demandera le nom de l'utiliseur, le creation s'il n"existe pas ou chargera le dictionnaire s'il existe et lui affichera son score actuel.
def recup_scores():
    if os.path.exists(liste_scores):
        fichier_scores = open(liste_scores, "rb")
        my_depickler= pickle.Unpickler(fichier_scores)
        scores = my_depickler.load()
        fichier_scores.close()
    else:
        scores = {}
    return scores

def save_scores(scores):
    fichier_scores = open(liste_scores, "wb")
    my_pickler=pickle.Pickler(fichier_scores)
    my_pickler.dump(scores)
    fichier_scores.close()

#fonction qui prendra un mot aleatoirement dans le dictionnaire liste_mots crée dans donnees.py
def choisir_mot_alea():
    mot_choisi_alea = random.choice(liste_mots)
    return mot_choisi_alea   # longueur que le mot a deviner, nous remplacerons ces characters
                                                              # par les bonnes lettres au fur et a mesure
 def mot_cacher():
    mot_a_deviner = "*" * len(mot_choisi_alea)      #nous creeons une ligne de characters composée de "*" de la meme
    return mot_a_deviner
#fonction qui demandera au joueur de taper une lettre, de lafficher si elle est bonne, ou retirer un continu si non

def info_lettres_utilisees(): #fonction qu'on utilisera avant demande_lettre pour informer le joueur des lettres qu'il a utilisé
    if len(lettre_utilisees)<1: #NB : pour la correction : j'utilise 3 fois if au lieu de if/elif/else , si je le fait pycharm me dit : "statement_expected, found py_ELSE_KEYWORD"
        print ("Il s'agit de votre premier essai.")
    if len(lettre_utilisees) == 1:
        print ("La lettre que vous avez utilisée précédemment est :", lettre_utilisees)
    if len(lettre_utilisees)>1:
        print ("Les lettres qui ont étés utilisées sont :", lettre_utilisees)

def demande_lettre():
    lettre_utilisateur = input("Tapez une lettre:")

    if len(lettre_utilisateur) < 1: #si l'utilisateur n'a rien tapé on renvoie la fonction pour redemander une lettre
        print ("Vous n'avez rien tapé!")
        return demande_lettre()

    elif len(lettre_utilisateur)>1: #même chose s'il y a plus de une lettre, on joue au pendu pas a motus
        print("Veuillez entrer une seule lettre")
        return demande_lettre()

    elif len(lettre_utilisateur) == 1 and type(lettre_utilisateur.lower()) != str: #on renvoie la fonction s'il ne s'agit pas d'une lettre
        print("Vous avez utilisé des caractères non autorisés")
        return demande_lettre()

    elif len (lettre_utilisateur) == 1 and type(lettre_utilisateur.lower()) == str and lettre_utilisateur in lettre_utilisees: #on verifie que l'utilisateur a bien entré une seule lettre et qu'elle n'a pas été utilisée ou qu'elle n'est pas utilisées
        print ("Cette lettre a été utilisée")
        return demande_lettre()

    else:
        lettre_utilisateur = lettre_utilisateur.lower()  # on met en minuscule la lettre entrée
        lettre_utilisees = lettre_utilisees + lettre_utilisateur  # on rajoute la lettre dans la string contenant les lettres utilisées pour eviter de processer deux fois la meme lettre
        return lettre_utilisees

def remplace_lettre():
    if lettre_utilisateur in mot_choisi_alea: #si lettre est dans le mot a trouver on continu sinon on passe de suite au retrait d'un point
        position_lettre = [index for index, value in enumerate(mot_choisi_alea) if value == lettre_utilisateur] #creation ou modification de la liste contenu la/les position(s) de(s) la lettre(s) entrée(s)
        mot_a_deviner = ''.join([lettre_utilisateur if i in position_lettre else a for i,a in enumerate(mot_a_deviner)]) #on joint les lettre en utilisant .join et la liste cree a la ligne au dessus
        print ("Une bonne lettre!")
        print (mot_a_deviner)
        return mot_a_deviner

    else:
        print ("Cette lettre ne fait pas partie du mot ! :(")
        chances_restantes -= 1
        return chances_restantes







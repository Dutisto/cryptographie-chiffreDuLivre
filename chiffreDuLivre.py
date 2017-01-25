import random

dico = {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[], 'H':[], 'I':[], 'J':[], 'K':[], 'L':[],
            'M':[], 'N':[], 'O':[], 'P':[], 'Q':[], 'R':[], 'S':[], 'T':[], 'U':[], 'V':[], 'W':[], 'X':[],
            'Y':[], 'Z':[], }


def supression(chaine):
#cette fonction utilise le code de la table ascii de chaque caractère de la chaine afin
#d'identifier si c'est une lettre. Si il ne s'agit pas d'une lettre, le supprime
    chaine = chaine.upper()
    for car in chaine:
        if -1 < ord(car) < 65 or 90 < ord(car) < 97 or 122 < ord(car):
            chaine = chaine.replace(car,"")
    return chaine

def dictionnaire(chaine):
#Cette fonction sert à compter le nombre d'occurence de chaque lettre avec leur indice dans la chaine à chaque occurence. On stocke tout ça dans un dictionnaire.
    dico = {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[], 'H':[], 'I':[], 'J':[], 'K':[], 'L':[],'M':[], 'N':[], 'O':[], 'P':[], 'Q':[], 'R':[], 'S':[], 'T':[], 'U':[], 'V':[], 'W':[], 'X':[],'Y':[], 'Z':[], }
    for key, values in dico.items():
        for i in range(len(chaine)):
            if chaine[i] == key:
                dico[key].append(i)
    return dico

def chiffrementLettre(lettre, clé):
#Si la lettre passé en paramètre existe dans la clé, on choisit une de ses valeurs de manière aléatoire.
    if clé[lettre]:
        lettreChiffre = random.choice(clé[lettre])
        return lettreChiffre

def chiffrage(texte, clé):
#On applique toutes les modifications nécessaires à la chaine et à la clé passé en paramètre. Puis on crypte le texte
    texteChiffre = []
    texte = supression(texte)
    clé = supression(clé)
    dico = dictionnaire(clé)
    for lettre in texte:
        if dico[lettre]:
            texteChiffre.append(chiffrementLettre(lettre, dico))
    print(texteChiffre)


def dechifrementLettre(valeur, clé):
#Si la valeur passée en paramètre fait partie de la clé, on retourne la lettre correspondante
        for c, v in clé.items():
            if valeur in v:
                return c



def dechiffrage(texte, clé):

    texteDechiffre = ""
    clé = supression(clé)
    dico = dictionnaire(clé)
    for car in texte:
        if car == ',':
            texte = texte.replace(car,'')
    ls = texte.split()
    for i, v in enumerate(ls):
        ls[i] = int(v)  if v.isdigit() else  float(v)
    #print(ls)
    for chiffre in ls:
        #if chiffre != ' ' and chiffre != ',' :
            caractere = dechifrementLettre(chiffre, dico)
            texteDechiffre = texteDechiffre + caractere
    print(texteDechiffre)


#texte = (219, 466, 859, 119, 868, 1602, 365, 107, 979, 1116, 1297, 1473, 1063, 620, 1089, 1134, 843, 49, 297, 640, 437, 1375, 736, 770, 906, 428, 395, 297, 752, 1151, 1182, 713, 543, 196, 1169, 912, 862, 298, 1249, 1541, 1675, 693, 568, 732, 1656, 4, 1480, 1075, 1126, 1359, 1699, 797, 907, 1711, 85, 820, 170, 479, 1725, 90, 160, 1159, 101, 287, 786, 439, 874, 1031, 640, 1092, 115, 542, 272, 1131, 538, 233, 566, 1454, 1523, 359, 944, 165, 1284, 1343, 1228, 96, 1028, 1060, 1055, 355, 992, 621, 1476, 826, 1243, 725, 1403, 1064, 1531, 838, 859, 771, 443, 591, 778, 1334, 728, 1053, 920, 25, 909, 1682, 146, 839, 1359, 896, 1518, 1446, 1496, 174, 1299, 1103, 1055, 77, 1190, 1631, 631, 875, 200, 1722, 1069, 965, 567, 661, 1421, 920, 1563, 403, 590, 1568, 1643, 43, 782, 349)
#clé ="Il existe 2 modalités d'obtention de Success Points à tout membre de la communauté SUPINFO International University ayant au moins le statut de Discovery Member. La première modalité d'obtention des Success Points est liée aux résultats académiques (notes) obtenus à travers les évaluations officielles des cursus SUPINFO. Ainsi, tous les points au dessus de 10/20 (moyenne) sont alors automatiquement crédités en Success Points sur un compte dédié après avoir été multipliés par le nombre de crédits ECTS affectés à la matière évaluée (ce qui correspond en quelque sorte à un coefficient). Par exemple, un étudiant qui obtient 17/20 dans une matière associée à 3 crédits ECTS verra son compte de Success Points crédité de 7*3 = 21 Success Points. La seconde modalité rend possible l'obtention de Success Points au travers d'actions remarquables au sein de la communauté : Organisation d'événements spéciaux évalués par les Campus Manager, publications d'articles remarquables et remarqués sur supinfo.com dans le cadre de la matière KWS (Knowledge Sharing) - modalité SCR (SUPINFO Certified Redactor), de projets d'exceptions, etc. Les conditions exactes d'obtention de points et le nombre de points attribués en fonction des actions sera communiqué dans le courant du second semestre de l'année civile 2015. Une bonne nouvelle : Dans le cadre du lancement des Success Points en 2015, le calcul des points attribués aux étudiants inscrits dans un cursus officiel à SUPINFO ces 5 dernières années est rétro-actif ! Si vous étiez déjà inscrit dans un cursus et avez obtenu des notes supérieures à la moyenne au cours de ces 5 dernières années, vous disposez probablement déjà d'un capital de Success Points reflétant votre performance académique des années écoulées. Pour le vérifier, rendez-vous vite sur Campus-Booster et en haut à droite de la fenêtre, juste sous votre nom, vous pouvez vérifier votre solde actuel de Success Points qui est affiché à côté de votre cumul de crédits ECTS. Un clic sur ce solde vous permettra d'afficher l'historique de toutes vos notes de manières, le coefficient ECTS correspondant et finalement, le nombre de Success Points obtenu. Une option spéciale \"Success Point\" a également été ajoutée à votre menu \"My Space"
#Pour modifier une clé, merci de bien vouloir modifier la ligne : cle = open(fichier, "r") où fichier est le
#fichier que vous désirez comme clé. Par défaut il s'agit de la clé donné avec l'énoncé.

fichierCle = "cleLivre.txt"
fichierCleEleve = "cleLivre.txt"
cle = open(fichierCleEleve, "r")
cle = cle.read()

#Pour modifier un chiffre, merci de bien vouloir modifier la ligne : cle = open(fichier, "r") où fichier est le
#fichier que vous désirez comme chiffre. Par défaut il s'agit du chiffre donné avec l'énoncé.

fichierChiffre = "chiffreLivre.txt"
fichierChiffreEleve = "chiffreLivreEleve.txt"
chiffre = open("test.txt", 'r')
chiffre = chiffre.read()
chiffreADechiffre = chiffre

chiffrage("Je suis un vrai cryptologue", cle)
dechiffrage(chiffre, cle)
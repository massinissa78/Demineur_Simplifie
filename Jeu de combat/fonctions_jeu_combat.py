import csv
import copy
from random import *

def lecture_fichier(nom_fichier:str):
    fichier_ouvert=open(nom_fichier,mode='r',encoding='utf-8')
    contenu=list(csv.reader(fichier_ouvert,delimiter=";"))
    fichier_ouvert.close()
    return contenu[0], contenu[1:]

def transformation_str_en_liste(text) :
    L = []
    debut = True
    for car in text :
        if car != '[' :
            if car =="'" :
                if debut:
                    mot = ''
                    debut = False
                else :
                    L.append(mot)
                    debut = True
            if car != "'" :
                mot+=car
    return L

def creation_dico(descripteurs : list, table:list) :
    dico = {}
    for personnage in table : # récupération des infos d'un personnage
        numero = int(personnage[0])
        dico[numero] = {}
        dico[numero]['Nom'] = personnage[1]
        dico[numero]['Classe'] = personnage[2]
        dico[numero]['PV'] = personnage[3]
        dico[numero]['Attaque'] = personnage[4]
        dico[numero]['Defense'] = personnage[5]
        dico[numero]['Magie'] = personnage[6]
        dico[numero]['Def_magique'] = personnage[7]
        dico[numero]['Vitesse'] = personnage[8]
        dico[numero]['Nom_fichier'] = personnage[9]
        dico[numero]['Nom_sprite'] = personnage[10]
        
    return dico
    
def affiche(dico:dict):
    for cle in dico[1].keys():
        print(cle.center(15), end=' | ')
    print("")
    for numero in dico.keys():
        personnage=dico[numero]
        for val in personnage.values():
            print(str(val).center(15),end=' | ')
        print('')

def liste_personnages(dico:dict):
    l=[]
    for cle,valeur in dico.items():
        l.append(dico[cle]['Nom'])
    return l

def selection_par_numero(n:int,dico:dict):
    d=copy.deepcopy(dico[n])
    return d

def selection_attaque(n:int,dico:dict):
    l=[]
    for cle in dico.keys():
        if int(dico[cle]['Attaque'])==n:
            l.append(dico[cle]['Nom'])
    return l

def selection_vitesse(n:int,dico:dict):
    l=[]
    for cle in dico.keys():
        if int(dico[cle]['Vitesse'])>=n:
            l.append(dico[cle]['Nom'])
    return l

def selection(dico:dict,champ,operateur,valeur,type_data):
    l=[]
    for cle in dico.keys():
        if eval(f"{type_data}('{dico[cle][champ]}'){operateur}{type_data}('{valeur}')")==True:
            l.append(dico[cle]['Nom'])
    return l

def attaque(attaquant:dict,defenseur:dict):
    if attaquant['Classe']=='Physique':
        calc_dgt=int(((int(attaquant['Attaque'])*1.1+int(attaquant['Vitesse'])*0.7)/(int(defenseur['Defense'])*0.6)+1)*randint(7,12))
        defenseur['PV']=int(defenseur['PV'])-calc_dgt
        if int(defenseur['PV'])<0:
            defenseur['PV']=0
    if attaquant['Classe']=='Magique':
        calc_dgt=int(((int(attaquant['Magie'])*1.1+int(attaquant['Vitesse'])*0.7)/(int(defenseur['Def_magique'])*0.6)+1)*randint(7,12))
        defenseur['PV']=int(defenseur['PV'])-calc_dgt
        if int(defenseur['PV'])<0:
            defenseur['PV']=0
    return attaquant,defenseur,calc_dgt
    
def ordre_attaque(personnage1:dict,personnage2:dict):
    if int(personnage1['Vitesse'])>int(personnage2['Vitesse']):
        return (personnage1,personnage2)
    else:
        return (personnage2,personnage1)

def combat(personnage1:dict,personnage2:dict):
    attaquant,defenseur=ordre_attaque(personnage1,personnage2)
    while int(attaquant['PV'])!=0 and int(defenseur['PV'])!=0:
        attaque(attaquant,defenseur)
        attaquant,defenseur=defenseur,attaquant
    if int(attaquant['PV'])==0:
        resultat=(defenseur,attaquant)
    if int(defenseur['PV'])==0:
        resultat=(attaquant,defenseur)
    return resultat
    
#main
descripteurs,table=lecture_fichier('personnages.csv')
dictionnaire=creation_dico(descripteurs,table)
affiche(dictionnaire)
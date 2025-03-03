import random

class Carte:
    
    def __init__(self,valeur:int,couleur:str,action:bool):
        self.valeur = valeur
        self.couleur = couleur
        self.action = action
    
    def dessiner_carte(self):
        return 'images/cartes/'+self.couleur+'_'+self.valeur+'.jpg'
    
    def __str__(self):
        info = 'La carte est un/une '+str(self.valeur)+', est de couleur '+self.couleur+' et'
        if self.action:
            info += ' est une carte action.'
        else:
            info += ' n\'est pas une carte action.'
        return info

class Paquet_de_Cartes:
    
    def __init__(self,liste_cartes:list):
        self.cartes = liste_cartes
        
    def nbr_cartes(self):
        return len(self.cartes)
    
    def premiere_carte(self,pioche): # Uniquement pour la défausse, en début de partie
        if self.nbr_cartes() == 0:
            for i in range(4):
                self.cartes.append('dos')
            self.cartes.append(random.choice(pioche.cartes)) # Nécessite d'avoir créé une pioche
            while self.cartes[4].valeur not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.cartes[4] = random.choice(pioche.cartes)
        
    def battre(self):
        random.shuffle(self.cartes)
        
    def ajouter(self,carte):
        self.cartes.append(carte)
        
    def distribution(self,n:int):
        paquet1=Paquet_de_Cartes([])
        paquet2=Paquet_de_Cartes([])
        for i in range(0,n,2):
            paquet1.cartes.append(self.cartes[i])
            paquet2.cartes.append(self.cartes[i+1])
        return paquet1,paquet2
    
    def affichage(self):
        for carte in self.cartes:
            print(carte)
            
    def tirer(self,x):
        if len(self.cartes)>0:
            carte_tiree=self.cartes[x]
            self.cartes.remove(carte_tiree)
            return carte_tiree
        else:
            return None

class Joueur:

    def __init__(self,nom:str,liste_cartes:list,nbr:int):
        self.nom = nom
        self.main = liste_cartes
        self.score = nbr
        
    def total_point(self):
        for carte in self.main:
            self.score += carte.valeur
    
    def reinitialiser(self):
        self.main = []

def jeu_50_cartes(couleur,valeur):
    lCartes = [i for i in range(50)]
    for i in range(48):
        if i <= 11:
            if 9 <= i <= 11:
                lCartes[i] = Carte(valeur[i],couleur[0],True)
            else:
                lCartes[i] = Carte(valeur[i],couleur[0],False)
        if 12 <=i <= 23:
            if 21 <= i <= 23:
                lCartes[i] = Carte(valeur[i-12],couleur[1],True)
            else:
                lCartes[i] = Carte(valeur[i-12],couleur[1],False)
        if 24 <=i <= 35:
            if 33 <= i <= 35:
                lCartes[i] = Carte(valeur[i-24],couleur[2],True)
            else:
                lCartes[i] = Carte(valeur[i-24],couleur[2],False)
        if 36 <=i <= 47:
            if 45 <= i <= 47:
                lCartes[i] = Carte(valeur[i-36],couleur[3],True)
            else:
                lCartes[i] = Carte(valeur[i-36],couleur[3],False)
    lCartes[48] = Carte(valeur[12],couleur[4],True)
    lCartes[49] = Carte(valeur[13],couleur[4],True)
    return lCartes

#main
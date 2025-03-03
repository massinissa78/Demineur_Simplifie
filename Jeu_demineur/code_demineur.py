import pygame
import random

def cases_adjacentes(grille):
    
    for ligne in range(len(grille.cases)):
        for colonne in range(len(grille.cases[ligne])):
            if not grille.cases[ligne][colonne] == "M":

                if 0<ligne<len(grille.cases)-1 and 0<colonne<len(grille.cases[ligne])-1:
                    
                    if grille.cases[ligne][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1

                elif ligne == 0 and 0<colonne<len(grille.cases[ligne])-1:
                    
                    if grille.cases[ligne][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                        
                elif 0<ligne<len(grille.cases)-1 and colonne == 0:
                    
                    if grille.cases[ligne][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1

                elif ligne == len(grille.cases)-1 and 0<colonne<len(grille.cases[ligne])-1:
                    
                    if grille.cases[ligne][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1

                elif 0<ligne<len(grille.cases)-1 and colonne == len(grille.cases[ligne])-1:
                    
                    if grille.cases[ligne][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                        
                elif ligne == len(grille.cases)-1 and colonne == len(grille.cases[ligne])-1:
                    
                    if grille.cases[ligne][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1

                elif ligne == len(grille.cases)-1 and colonne == 0:
                    
                    if grille.cases[ligne][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne-1][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1

                elif ligne == 0 and colonne == len(grille.cases[ligne])-1:
                    
                    if grille.cases[ligne][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne-1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1

                elif ligne == 0 and colonne == 0:
                    
                    if grille.cases[ligne][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne] == "M":
                        grille.cases[ligne][colonne] += 1
                    if grille.cases[ligne+1][colonne+1] == "M":
                        grille.cases[ligne][colonne] += 1

    return grille

class Grille :
    
    def __init__(self,taille_case,cases_long,cases_haut):
        self.taille_case = taille_case
        self.cases_long = cases_long
        self.cases_haut = cases_haut
        self.cases = []
        self.cases_clic = []
        self.cases_drapeau = []
        
    def creation(self):
        L = []
        l = []
        ll = []
        for i in range(self.cases_haut):
            L2 = []
            for j in range(self.cases_long):
                L2.append(0)
            L.append(L2)
        self.cases = L
        for i in range(self.cases_haut):
            l2 = []
            for j in range(self.cases_long):
                l2.append(False)
            l.append(l2)
        self.cases_clic = l
        for i in range(self.cases_haut):
            ll2 = []
            for j in range(self.cases_long):
                ll2.append(False)
            ll.append(ll2)
        self.cases_drapeau = ll
    
    def placer_mines(self):
        plage = [i for i in range(self.cases_long)]
        for i in range(50):
            ligne = random.choice(plage)
            colonne = random.choice(plage)
            while self.cases[ligne][colonne] == "M":
                ligne = random.choice(plage)
                colonne = random.choice(plage)
            if self.cases[ligne][colonne] == 0:
                self.cases[ligne][colonne] = "M"
    
    def calibrage(self):
        cases_adjacentes(self)
        
    def reinitialiser(self):
        self.creation()
        self.placer_mines()
        self.calibrage()
        
class FenetreJeu:
    """
    Classe qui gère la fenêtre principale du jeu.
    """
    def __init__(self, largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.en_cours = True  # Variable pour savoir si le jeu tourne

        # Initialisation de pygame et création de la fenêtre
        pygame.init()
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(self.titre)
        
        # Couleurs
        self.couleur_fond = (48, 89, 112)  # Bleu foncé
        self.couleur_case = (149, 211, 219) # Bleu clair
        self.couleur_case_cliquee = (255, 255, 255) # Blanc
        self.couleur_drapeau = (255, 0, 0) # Rouge
        self.couleur_texte = (0, 0, 0) # Noir

        # Bouton "Jouer"
        bouton_largeur = 200
        bouton_hauteur = 50
        self.bouton_jouer = pygame.Rect(self.largeur // 2 - bouton_largeur // 2, self.hauteur // 2 + 100, bouton_largeur, bouton_hauteur)
        self.bouton_rejouer = pygame.Rect(100, self.hauteur // 2 + 100, bouton_largeur, bouton_hauteur)
        self.bouton_quitter = pygame.Rect(400, self.hauteur // 2 + 100, bouton_largeur, bouton_hauteur)
        
        # Marges et espacement
        self.marge_gauche = 35
        self.marge_haut = 25
        self.espacement_cases = 6

        # Variables pour le jeu principal
        self.cases = {}
        self.jeu_commence = False
        self.nbr_drapeaux = 50
        self.nbr_cases_clic = 0
        self.fin_jeu = False
        self.perdu = False
        self.gagne = False
        self.rejouer = 0

    def lancer_jeu(self):
        """
        Boucle principale du jeu.
        """
        self.musique()
        while self.en_cours:
            self.boucle_jeu()     # Mise à jour les variables
            self.dessiner()          # Rendu graphique
            pygame.display.flip()   # Mise à jour de l'écran
        pygame.quit()
        
    def musique(self):
        """
        Lance aléatoirement une musique parmi 4 disponibles.
        """
        #m = random.randint(1,4)
        #pygame.mixer.music.load(str('musiques/musique'+str(m)+'.mp3'))
        #pygame.mixer.music.set_volume(0.2)
        #pygame.mixer.music.play(-1)
        
    def cases_adjacentes(self,grille,ligne,colonne):
        """
        Dévoile les cases adjacentes lorsque le joueur clique sur une case proche d'aucune mine.
        """
        if 0<ligne<len(grille.cases)-1 and 0<colonne<len(grille.cases[ligne])-1:
            
            if grille.cases[ligne][colonne-1] != "M" and not grille.cases_drapeau[ligne][colonne-1]:
                if not grille.cases_clic[ligne][colonne-1]:
                    grille.cases_clic[ligne][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne][colonne+1] != "M" and not grille.cases_drapeau[ligne][colonne+1]:
                if not grille.cases_clic[ligne][colonne+1]:
                    grille.cases_clic[ligne][colonne+1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne-1] != "M" and not grille.cases_drapeau[ligne-1][colonne-1]:
                if not grille.cases_clic[ligne-1][colonne-1]:
                    grille.cases_clic[ligne-1][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne] != "M" and not grille.cases_drapeau[ligne-1][colonne]:
                if not grille.cases_clic[ligne-1][colonne]:
                    grille.cases_clic[ligne-1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne+1] != "M" and not grille.cases_drapeau[ligne-1][colonne+1]:
                if not grille.cases_clic[ligne-1][colonne+1]:
                    grille.cases_clic[ligne-1][colonne+1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne-1] != "M" and not grille.cases_drapeau[ligne+1][colonne-1]:
                if not grille.cases_clic[ligne+1][colonne-1]:
                    grille.cases_clic[ligne+1][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne] != "M" and not grille.cases_drapeau[ligne+1][colonne]:
                if not grille.cases_clic[ligne+1][colonne]:
                    grille.cases_clic[ligne+1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne+1] != "M" and not grille.cases_drapeau[ligne+1][colonne+1]:
                if not grille.cases_clic[ligne+1][colonne+1]:
                    grille.cases_clic[ligne+1][colonne+1] = True
                    self.nbr_cases_clic += 1

        elif ligne == 0 and 0<colonne<len(grille.cases[ligne])-1:
            
            if grille.cases[ligne][colonne-1] != "M" and not grille.cases_drapeau[ligne][colonne-1]:
                if not grille.cases_clic[ligne][colonne-1]:
                    grille.cases_clic[ligne][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne][colonne+1] != "M" and not grille.cases_drapeau[ligne][colonne+1]:
                if not grille.cases_clic[ligne][colonne+1]:
                    grille.cases_clic[ligne][colonne+1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne-1] != "M" and not grille.cases_drapeau[ligne+1][colonne-1]:
                if not grille.cases_clic[ligne+1][colonne-1]:
                    grille.cases_clic[ligne+1][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne] != "M" and not grille.cases_drapeau[ligne+1][colonne]:
                if not grille.cases_clic[ligne+1][colonne]:
                    grille.cases_clic[ligne+1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne+1] != "M" and not grille.cases_drapeau[ligne+1][colonne+1]:
                if not grille.cases_clic[ligne+1][colonne+1]:
                    grille.cases_clic[ligne+1][colonne+1] = True
                    self.nbr_cases_clic += 1
                
        elif 0<ligne<len(grille.cases)-1 and colonne == 0:
            
            if grille.cases[ligne][colonne+1] != "M" and not grille.cases_drapeau[ligne][colonne+1]:
                if not grille.cases_clic[ligne][colonne+1]:
                    grille.cases_clic[ligne][colonne+1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne] != "M" and not grille.cases_drapeau[ligne-1][colonne]:
                if not grille.cases_clic[ligne-1][colonne]:
                    grille.cases_clic[ligne-1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne+1] != "M" and not grille.cases_drapeau[ligne-1][colonne+1]:
                if not grille.cases_clic[ligne-1][colonne+1]:
                    grille.cases_clic[ligne-1][colonne+1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne] != "M" and not grille.cases_drapeau[ligne+1][colonne]:
                if not grille.cases_clic[ligne+1][colonne]:
                    grille.cases_clic[ligne+1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne+1] != "M" and not grille.cases_drapeau[ligne+1][colonne+1]:
                if not grille.cases_clic[ligne+1][colonne+1]:
                    grille.cases_clic[ligne+1][colonne+1] = True
                    self.nbr_cases_clic += 1

        elif ligne == len(grille.cases)-1 and 0<colonne<len(grille.cases[ligne])-1:
            
            if grille.cases[ligne][colonne-1] != "M" and not grille.cases_drapeau[ligne][colonne-1]:
                if not grille.cases_clic[ligne][colonne-1]:
                    grille.cases_clic[ligne][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne][colonne+1] != "M" and not grille.cases_drapeau[ligne][colonne+1]:
                if not grille.cases_clic[ligne][colonne+1]:
                    grille.cases_clic[ligne][colonne+1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne-1] != "M" and not grille.cases_drapeau[ligne-1][colonne-1]:
                if not grille.cases_clic[ligne-1][colonne-1]:
                    grille.cases_clic[ligne-1][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne] != "M" and not grille.cases_drapeau[ligne-1][colonne]:
                if not grille.cases_clic[ligne-1][colonne]:
                    grille.cases_clic[ligne-1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne+1] != "M" and not grille.cases_drapeau[ligne-1][colonne+1]:
                if not grille.cases_clic[ligne-1][colonne+1]:
                    grille.cases_clic[ligne-1][colonne+1] = True
                    self.nbr_cases_clic += 1

        elif 0<ligne<len(grille.cases)-1 and colonne == len(grille.cases[ligne])-1:
            
            if grille.cases[ligne][colonne-1] != "M" and not grille.cases_drapeau[ligne][colonne-1]:
                if not grille.cases_clic[ligne][colonne-1]:
                    grille.cases_clic[ligne][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne-1] != "M" and not grille.cases_drapeau[ligne-1][colonne-1]:
                if not grille.cases_clic[ligne-1][colonne-1]:
                    grille.cases_clic[ligne-1][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne] != "M" and not grille.cases_drapeau[ligne-1][colonne]:
                if not grille.cases_clic[ligne-1][colonne]:
                    grille.cases_clic[ligne-1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne-1] != "M" and not grille.cases_drapeau[ligne+1][colonne-1]:
                if not grille.cases_clic[ligne+1][colonne-1]:
                    grille.cases_clic[ligne+1][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne] != "M" and not grille.cases_drapeau[ligne+1][colonne]:
                if not grille.cases_clic[ligne+1][colonne]:
                    grille.cases_clic[ligne+1][colonne] = True
                    self.nbr_cases_clic += 1
                
        elif ligne == len(grille.cases)-1 and colonne == len(grille.cases[ligne])-1:
            
            if grille.cases[ligne][colonne-1] != "M" and not grille.cases_drapeau[ligne][colonne-1]:
                if not grille.cases_clic[ligne][colonne-1]:
                    grille.cases_clic[ligne][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne-1] != "M" and not grille.cases_drapeau[ligne-1][colonne-1]:
                if not grille.cases_clic[ligne-1][colonne-1]:
                    grille.cases_clic[ligne-1][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne] != "M" and not grille.cases_drapeau[ligne-1][colonne]:
                if not grille.cases_clic[ligne-1][colonne]:
                    grille.cases_clic[ligne-1][colonne] = True
                    self.nbr_cases_clic += 1

        elif ligne == len(grille.cases)-1 and colonne == 0:
            
            if grille.cases[ligne][colonne+1] != "M" and not grille.cases_drapeau[ligne][colonne+1]:
                if not grille.cases_clic[ligne][colonne+1]:
                    grille.cases_clic[ligne][colonne+1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne] != "M" and not grille.cases_drapeau[ligne-1][colonne]:
                if not grille.cases_clic[ligne-1][colonne]:
                    grille.cases_clic[ligne-1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne-1][colonne+1] != "M" and not grille.cases_drapeau[ligne-1][colonne+1]:
                if not grille.cases_clic[ligne-1][colonne+1]:
                    grille.cases_clic[ligne-1][colonne+1] = True
                    self.nbr_cases_clic += 1

        elif ligne == 0 and colonne == len(grille.cases[ligne])-1:
            
            if grille.cases[ligne][colonne-1] != "M" and not grille.cases_drapeau[ligne][colonne-1]:
                if not grille.cases_clic[ligne][colonne-1]:
                    grille.cases_clic[ligne][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne-1] != "M" and not grille.cases_drapeau[ligne+1][colonne-1]:
                if not grille.cases_clic[ligne+1][colonne-1]:
                    grille.cases_clic[ligne+1][colonne-1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne] != "M" and not grille.cases_drapeau[ligne+1][colonne]:
                if not grille.cases_clic[ligne+1][colonne]:
                    grille.cases_clic[ligne+1][colonne] = True
                    self.nbr_cases_clic += 1

        elif ligne == 0 and colonne == 0:
            
            if grille.cases[ligne][colonne+1] != "M" and not grille.cases_drapeau[ligne][colonne+1]:
                if not grille.cases_clic[ligne][colonne+1]:
                    grille.cases_clic[ligne][colonne+1] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne] != "M" and not grille.cases_drapeau[ligne+1][colonne]:
                if not grille.cases_clic[ligne+1][colonne]:
                    grille.cases_clic[ligne+1][colonne] = True
                    self.nbr_cases_clic += 1
            if grille.cases[ligne+1][colonne+1] != "M" and not grille.cases_drapeau[ligne+1][colonne+1]:
                if not grille.cases_clic[ligne+1][colonne+1]:
                    grille.cases_clic[ligne+1][colonne+1] = True
                    self.nbr_cases_clic += 1

    def boucle_jeu(self):
        """
        Boucle de jeu
        """
        if not self.fin_jeu: # Tant que le joueur est en jeu
            
            for event in pygame.event.get(): # Attente des évènements
                
                if event.type == pygame.QUIT: # Si le jeu est quitté
                    self.en_cours = False
                
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # Si le joueur fait un clic gauche
                    
                    if self.bouton_jouer.collidepoint(event.pos) and not self.jeu_commence: # Si le joueur clique sur "Jouer"
                        print("Le jeu commence !")
                        self.jeu_commence = True
                    
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Si le joueur fait un clic gauche
                    
                    for ligne in self.cases.keys():
                        for colonne,val in self.cases[ligne].items():
                            if val.collidepoint(event.pos) and self.jeu_commence: # Si le joueur clique sur une case de la grille
                                
                                if grille.cases[ligne][colonne] in [0,1,2,3,4,5,6,7,8] and not grille.cases_drapeau[ligne][colonne]:
                                    if not grille.cases_clic[ligne][colonne]:
                                        self.nbr_cases_clic += 1
                                        grille.cases_clic[ligne][colonne] = True
                                    if grille.cases[ligne][colonne] == 0:
                                        self.cases_adjacentes(grille,ligne,colonne)
                                    if self.nbr_cases_clic == grille.cases_long * grille.cases_haut - 50 :
                                        self.gagne = True
                                        
                                elif grille.cases[ligne][colonne] == "M" and not grille.cases_drapeau[ligne][colonne]:
                                    grille.cases_clic[ligne][colonne] = True
                                    for ligne2 in range(len(grille.cases)):
                                        for colonne2 in range(len(grille.cases[ligne])):
                                            if grille.cases[ligne2][colonne2] == 'M':
                                                grille.cases_clic[ligne2][colonne2] = True
                                    self.perdu = True
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: # Si le joueur fait un clic droit
                    
                    for ligne in self.cases.keys():
                        for colonne,val in self.cases[ligne].items():
                            if val.collidepoint(event.pos) and self.jeu_commence: # Si le joueur clique sur une case de la grille

                                if not grille.cases_clic[ligne][colonne]:
                                    if self.nbr_drapeaux > 0:
                                        if not grille.cases_drapeau[ligne][colonne]:
                                            grille.cases_drapeau[ligne][colonne] = True
                                            self.nbr_drapeaux -= 1
                                        else:
                                            grille.cases_drapeau[ligne][colonne] = False
                                            self.nbr_drapeaux += 1
                                            
        if self.fin_jeu:
            
            for event in pygame.event.get(): # Attente des évènements
            
                if event.type == pygame.QUIT: # Si le jeu est quitté
                    self.en_cours = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Si le joueur fait un clic gauche
                    
                    if self.bouton_rejouer.collidepoint(event.pos): # Si le joueur clique sur "Rejouer"
                        print("Le jeu recommence !")
                        self.rejouer = 1
                        # Réinitialisation des attributs de FenetreJeu
                        self.reinitialiser_jeu()
                        
                    if self.bouton_quitter.collidepoint(event.pos): # Si le joueur clique sur "Quitter"
                        print("Fin du jeu !")
                        self.rejouer = 2  
                                
    def reinitialiser_jeu(self):
        """
        Réinitialise les attributs du jeu pour une nouvelle partie.
        """
        grille.reinitialiser()
        self.cases = {}  # Redéfinir le dictionnaire des cases
        self.jeu_commence = False
        self.nbr_drapeaux = 50
        self.nbr_cases_clic = 0
        self.fin_jeu = False
        self.perdu = False
        self.gagne = False
        self.rejouer = 0
        
    def dessiner(self):
        """
        Dessine le contenu du jeu à l'écran.
        """
        
        # Chargement des images du jeu
        for i in range(grille.cases_haut):
            self.cases[i] = {}
            for j in range(grille.cases_long):
                self.cases[i][j] = pygame.Rect(110 + j*(grille.taille_case + 7), 90 + i*(grille.taille_case + 7), grille.taille_case, grille.taille_case)
        
        image_fond = pygame.image.load('images/fond.jpg').convert_alpha()
        image_fond= pygame.transform.scale(image_fond,(self.largeur,self.hauteur))
        image_case = pygame.image.load('images/case.png').convert_alpha()
        image_case_clic = pygame.image.load('images/case_clic.png').convert_alpha()
        image_bombe = pygame.image.load('images/bombe.png').convert_alpha()
        image_drapeau = pygame.image.load('images/drapeau.png').convert_alpha()
        image_bouton_jouer = pygame.image.load('images/bouton_jouer.png').convert_alpha()
        image_bouton_rejouer = pygame.image.load('images/bouton_rejouer.png').convert_alpha()
        image_bouton_quitter = pygame.image.load('images/bouton_quitter.png').convert_alpha()
        image_titre_jeu = pygame.image.load('images/titre_jeu.png').convert_alpha()
        image_titre_jeu = pygame.transform.scale(image_titre_jeu,(500,76))
                
        # Chargement des polices et d'images supplémentaires
        pol1 = pygame.font.SysFont('Bahnschrift',30,italic=True,bold=True)
        pol2 = pygame.font.SysFont('Bahnschrift',65,italic=True,bold=True)
        pol3 = pygame.font.SysFont('Bahnschrift', int(grille.taille_case * 0.6), italic=True, bold=True)
        pol4 = pygame.font.SysFont('Bahnschrift',45,italic=True,bold=True)
        
        if not self.jeu_commence: # Menu d'ouverture
            
            self.fenetre.blit(image_fond,(0,0))  # Fond d'écran
            self.fenetre.blit(image_titre_jeu,(100,160))
            self.fenetre.blit(image_bouton_jouer,self.bouton_jouer)
            police2 = pygame.font.SysFont('Bahnschrift', 36)
            txt_nom = police2.render("Massinissa Bendahmane TG3", True, (255, 255, 255))
            self.fenetre.blit(txt_nom, (self.marge_gauche, self.marge_haut))
            
        elif self.jeu_commence and not self.fin_jeu: # Pendant la partie
            
            self.fenetre.blit(image_fond,(0,0))  # Fond d'écran
            pygame.draw.rect(self.fenetre, self.couleur_fond, (100, 80, grille.cases_long*grille.taille_case + grille.cases_long*7 + 10, grille.cases_haut*grille.taille_case + grille.cases_haut*7 + 10))
            for ligne in self.cases.keys() :
                for colonne in self.cases[ligne].keys():
                    self.fenetre.blit(image_case, self.cases[ligne][colonne])
                    if grille.cases_clic[ligne][colonne]:
                        self.fenetre.blit(image_case_clic, self.cases[ligne][colonne])
                        if grille.cases[ligne][colonne] == 'M':
                            self.fenetre.blit(image_bombe, self.cases[ligne][colonne])
                        else :
                            num = pol3.render(str(grille.cases[ligne][colonne]), True, (0,0,0))
                            self.fenetre.blit(num, (self.cases[ligne][colonne]))
                    if grille.cases_drapeau[ligne][colonne]:
                        self.fenetre.blit(image_drapeau, self.cases[ligne][colonne])
            pygame.draw.rect(self.fenetre, (255, 255, 255), (230, 15, 250, 60))
            pygame.draw.rect(self.fenetre, (0,0,0), (235, 20, 240, 50))
            pygame.draw.rect(self.fenetre, (255, 255, 255), (350, 15, 5, 60))
            txt_drapeau = pol4.render(str(self.nbr_drapeaux), True, (255,255,255))
            self.fenetre.blit(txt_drapeau,(240,25))
            image_drapeau = pygame.transform.scale(image_drapeau,(40,40))
            self.fenetre.blit(image_drapeau,(310,25))
            txt_cases_clic = pol4.render(str(self.nbr_cases_clic), True, (255,255,255))
            self.fenetre.blit(txt_cases_clic,(355,25))
            image_case = pygame.transform.scale(image_case,(40,40))
            self.fenetre.blit(image_case,(430,25))
            
            if self.perdu or self.gagne :
                self.fin_jeu = True

        elif self.fin_jeu: # Ecran de victoire/défaite
            
            pygame.time.wait(1400)
            self.fenetre.blit(image_fond,(0,0))  # Fond d'écran
            
            if self.perdu :
                pygame.draw.rect(self.fenetre, self.couleur_fond, (170, 90, 365, 150))
                txt_perdu1 = pol2.render("Dommage !", True, (255, 255, 255))
                txt_perdu2 = pol1.render("Vous avez perdu !", True, (255, 255, 255))
                self.fenetre.blit(txt_perdu1, (180, 100))
                self.fenetre.blit(txt_perdu2, (225, 190))
                self.fenetre.blit(image_bouton_rejouer,self.bouton_rejouer)
                self.fenetre.blit(image_bouton_quitter,self.bouton_quitter)
            
            else :
                pygame.draw.rect(self.fenetre, self.couleur_fond, (170, 90, 345, 150))
                txt_gagne1 = pol2.render("Bien joué !", True, (255, 255, 255))
                txt_gagne2 = pol1.render("Vous avez gagné !", True, (255, 255, 255))
                self.fenetre.blit(txt_gagne1, (189, 100))
                self.fenetre.blit(txt_gagne2, (225, 190))
                self.fenetre.blit(image_bouton_rejouer,self.bouton_rejouer)
                self.fenetre.blit(image_bouton_quitter,self.bouton_quitter)
                
            if self.rejouer == 2:
                pygame.display.flip()
                pygame.time.wait(2600)
                self.en_cours = False
            
# Main
grille = Grille(24,16,16)
grille.creation()
grille.placer_mines()
grille.calibrage()

jeu = FenetreJeu(700, 600, "Démineur")
jeu.lancer_jeu()

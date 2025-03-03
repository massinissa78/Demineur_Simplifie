import pygame
from jeu_cartes import *

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

        # Bouton "Jouer"
        self.bouton_jouer = pygame.Rect(self.largeur // 2 - 100, self.hauteur // 2 + 100, 200, 50)

        # Variables pour le jeu principal
        self.jeu_commence = False
        self.tour_ordi = False
        self.tour_joueur = True
        self.tour_supplementaire_ordi = False
        self.piocher = False
        self.uno = False
        self.fin_jeu = False

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
        m = random.randint(1,4)
        pygame.mixer.music.load(str('musiques/musique'+str(m)+'.mp3'))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        
    def verif_carte(self,carte,carte_defausse):
        """
        Méthode appelée pour vérifier qu'une carte peut être placée légalement par un joueur.
        """
        verif = False
        if carte.valeur == carte_defausse.valeur: # Si les cartes ont la même valeur
            verif = True
        elif carte.couleur == carte_defausse.couleur: # Si les cartes sont de même couleur
            verif = True
        elif carte.action == carte_defausse.action and carte.action == True: # Si 2 cartes actions sont superposées
            if carte.valeur == carte_defausse.valeur or carte.couleur == carte_defausse.couleur or carte.valeur == 'couleur' or carte.valeur == 'plus4':# Conditions précedentes, sauf si plus 2 ou joker
                verif = True
        elif carte.valeur == 'plus4' or carte.valeur == 'couleur': # Automatiquement vérifié si plus 2 ou joker
            verif = True
        return verif # Le jeu peut avoir lieu si l'une des conditions a été vérifiée
    
    def action_carte(self,carte):
        """
        Méthode qui retourne l'éventuelle action causée en posant la carte.
        Action 1 : Tour sauté
        Action 2 : Cartes piochées de force
        Action 3 : Couleur changée (aléatoirement)
        Action 4 : Addition des 2 précédentes actions
        """
        action = 0
        if carte.valeur == 'plus4':
            action = 4
        elif carte.valeur == 'couleur':
            action = 3
        elif carte.valeur == 'interdit' or carte.valeur == 'inverse':
            action = 1
        elif carte.valeur == 'plus2':
            action = 2
        return action
    
    def contre_uno(self):
        """
        Méthode appelée si le joueur n'a plus qu'une seule carte mais n'a pas déclaré UNO.
        """
        for i in range(2):
            main_joueur.ajouter(random.choice(pioche.cartes)) # Le joueur pioche 2 cartes
    def boucle_jeu(self):
        """
        Boucle de jeu
        """
        if not self.fin_jeu: # Tant que personne n'a de main vide
            
            if len(main_joueur.cartes) > 0:
                distance = 560 / len(main_joueur.cartes) # Calcul de l'espacement des cartes, pour l'affichage et la sélection
                
            if self.tour_ordi: # Tour de l'ordi
                self.piocher = False
                self.tour_supplementaire_ordi = False
                self.tour_joueur = False # Remise à 0 des variables
                if len(main_ordi.cartes) == 0: # Si l'ordi n'a plus de cartes (variable vérifiée si l'ordi enchaîne plusieurs tours)
                    self.fin_jeu = True
                cartes_dispo = len(main_ordi.cartes) # Liste à parcourir pour choisir quelle carte jouer
                verif = self.verif_carte(main_ordi.cartes[cartes_dispo-1],defausse.cartes[len(defausse.cartes)-1]) # Vérifier que la carte peut être placée
                while not verif: # Tant que l'ordi ne choisit pas une carte valable
                    cartes_dispo -= 1 # Passage à la carte suivante
                    if cartes_dispo == 0: # S'il ne peut rien jouer
                        main_ordi.ajouter(random.choice(pioche.cartes))
                        print("Carte piochée ordi")
                        self.piocher = True
                        verif = True # L'ordi pioche une carte et saute la vérification
                    elif cartes_dispo > 0:
                        verif = self.verif_carte(main_ordi.cartes[cartes_dispo-1],defausse.cartes[len(defausse.cartes)-1]) # Réitère la vérification
                        
                if not self.piocher: # Si l'ordi peut jouer une carte
                    carte_jouee = main_ordi.tirer(cartes_dispo-1) 
                    defausse.cartes.append(carte_jouee) # Retrait de la carte jouée, ajoutée à la défausse
                    print("Carte jouée ordi")
                    if len(main_ordi.cartes) == 0: # Si l'ordi n'a plus de cartes
                        self.fin_jeu = True
                    action = self.action_carte(carte_jouee) # Appel des possibles actions de la carte
                    if action == 1:
                        self.tour_supplementaire_ordi = True # L'ordi rejoue
                    elif action == 2:
                        for i in range(2):
                            main_joueur.ajouter(random.choice(pioche.cartes)) # Le joueur pioche 2 cartes
                    elif action == 3:
                        defausse.cartes.append(random.choice([bleu_0,rouge_0,vert_0,jaune_0])) # La couleur change (carte sans valeur)
                    elif action == 4:
                        for i in range(4):
                            main_joueur.ajouter(random.choice(pioche.cartes))
                        defausse.cartes.append(random.choice([bleu_0,rouge_0,vert_0,jaune_0])) # La couleur change et le joueur pioche 4 cartes
                self.tour_ordi = False
                self.uno = False
                pygame.time.wait(1300)
                
            for event in pygame.event.get(): # Attente des évènements
                
                if event.type == pygame.QUIT: # Si le jeu est quitté
                    self.en_cours = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN: # Si le joueur clique
                    
                    if self.bouton_jouer.collidepoint(event.pos) and not self.jeu_commence: # Si le joueur clique sur "Jouer"
                        print("Le jeu commence !")
                        self.jeu_commence = True
                        
                    if self.tour_joueur: # Si le tour est au joueur
                        self.piocher = False
                        if event.button == 1 and self.jeu_commence: # Si clic gauche pressé
                            clic_x = event.pos[0]
                            clic_y = event.pos[1]
                            
                            if 330 <= clic_x <= 330+lrg_carte and 209 <= clic_y <= 209+lng_carte: # Si le joueur clique sur la pioche
                                main_joueur.ajouter(random.choice(pioche.cartes))
                                print("Carte piochée")
                                self.piocher = True
                                self.tour_ordi = True # Fin du tour
                                
                            elif 170 <= clic_x <= 730 and self.hauteur-lng_carte <= clic_y <= self.hauteur: # Si le joueur clique sur sa main
                                for i in range(len(main_joueur.cartes)): # Parcours des zones des différentes cartes
                                    
                                    if len(main_joueur.cartes) <= 7: # Si les cartes ne se superposent pas
                                        if 170+i*lrg_carte <= clic_x <= 170+(i+1)*lrg_carte and self.hauteur-lng_carte <= clic_y <= self.hauteur:
                                            verif = self.verif_carte(main_joueur.cartes[i],defausse.cartes[len(defausse.cartes)-1]) # Vérifier si la carte peut être placée
                                            if verif == True:
                                                carte_jouee = main_joueur.tirer(i)
                                                defausse.cartes.append(carte_jouee) # Retrait de la carte jouée, ajoutée à la défausse
                                                print("Carte jouée")
                                                if len(main_joueur.cartes) == 1 and not self.uno: # Si le joueur avait 2 cartes et n'a pas appuyé sur "UNO"
                                                    self.contre_uno()
                                                    print("Contre-UNO !")
                                                if len(main_joueur.cartes) == 0: # Si la main du joueur est vide
                                                    self.fin_jeu = True
                                                action = self.action_carte(carte_jouee) # Appel des possibles actions de la carte
                                                if action == 1:
                                                    self.tour_ordi = False # Le joueur rejoue
                                                elif action == 2:
                                                    for i in range(2):
                                                        main_ordi.ajouter(random.choice(pioche.cartes)) # L'ordi pioche 2 cartes
                                                    self.tour_ordi = True
                                                elif action == 3:
                                                    defausse.cartes.append(random.choice([bleu_0,rouge_0,vert_0,jaune_0])) # La couleur est changée
                                                    self.tour_ordi = True
                                                elif action == 4:
                                                    for i in range(4):
                                                        main_ordi.ajouter(random.choice(pioche.cartes))
                                                    defausse.cartes.append(random.choice([bleu_0,rouge_0,vert_0,jaune_0])) # La couleur est changée et l'ordi pioche 4 cartes
                                                    self.tour_ordi = True
                                                else:
                                                    self.tour_ordi = True # Si la carte n'est pas active, rien ne se passe
                                                    
                                    else: # Si les cartes se superposent (main supérieure à 7 cartes)
                                        if 170+i*distance <= clic_x <= 170+(i+1)*distance and self.hauteur-lng_carte <= clic_y <= self.hauteur:
                                            verif = self.verif_carte(main_joueur.cartes[i],defausse.cartes[len(defausse.cartes)-1]) # Vérifier si la carte peut être placée
                                            if verif == True:
                                                carte_jouee = main_joueur.tirer(i)
                                                defausse.cartes.append(carte_jouee) # Retrait de la carte jouée, ajoutée à la défausse
                                                print("Carte jouée")
                                                if len(main_joueur.cartes) == 1 and not self.uno: # Si le joueur avait 2 cartes et n'a pas appuyé sur "UNO"
                                                    self.contre_uno()
                                                    print("Contre-UNO !")
                                                if len(main_joueur.cartes) == 0: # Si la main du joueur est vide
                                                    self.fin_jeu = True
                                                action = self.action_carte(carte_jouee) # Appel des possibles actions de la carte
                                                if action == 1:
                                                    self.tour_ordi = False # Le joueur rejoue
                                                elif action == 2:
                                                    for i in range(2):
                                                        main_ordi.ajouter(random.choice(pioche.cartes)) # L'ordi pioche 2 cartes
                                                    self.tour_ordi = True
                                                elif action == 3:
                                                    defausse.cartes.append(random.choice([bleu_0,rouge_0,vert_0,jaune_0])) # La couleur est changée
                                                    self.tour_ordi = True
                                                elif action == 4:
                                                    for i in range(4):
                                                        main_ordi.ajouter(random.choice(pioche.cartes))
                                                    defausse.cartes.append(random.choice([bleu_0,rouge_0,vert_0,jaune_0])) # La couleur est changée et l'ordi pioche 4 cartes
                                                    self.tour_ordi = True
                                                else:
                                                    self.tour_ordi = True # Si la carte n'est pas active, rien ne se passe
                            elif 720 <= clic_x <= 900 and 240 <= clic_y <= 360 and len(main_joueur.cartes) == 2 and not self.uno: # Si le joueur clique sur le bouton UNO
                                self.uno = True
                                
            if self.tour_supplementaire_ordi:
                self.tour_ordi = True
            if self.tour_ordi:
                self.tour_joueur = False
            else:
                self.tour_joueur = True # Passage du tour à l'adversaire, sauf si l'un enchaîne plusieurs cartes
                
    def dessiner(self):
        """
        Dessine le contenu du jeu à l'écran.
        """
        
        # Chargement des images des cartes
        images_cartes={}
        for carte in liste_cartes:
            images_cartes[str(carte.couleur+'_'+carte.valeur)]=pygame.image.load(carte.dessiner_carte()).convert_alpha()
            images_cartes[str(carte.couleur+'_'+carte.valeur)]=pygame.transform.scale(images_cartes[str(carte.couleur+'_'+carte.valeur)],(lrg_carte,lng_carte))
        images_cartes['dos']=pygame.image.load('images/cartes/dos.jpg').convert_alpha()
        images_cartes['dos']=pygame.transform.scale(images_cartes['dos'],(lrg_carte,lng_carte))
        images_cartes['bleu_0']=pygame.image.load('images/cartes/bleu_0.jpg').convert_alpha()
        images_cartes['bleu_0']=pygame.transform.scale(images_cartes['bleu_0'],(lrg_carte,lng_carte))
        images_cartes['vert_0']=pygame.image.load('images/cartes/vert_0.jpg').convert_alpha()
        images_cartes['vert_0']=pygame.transform.scale(images_cartes['vert_0'],(lrg_carte,lng_carte))
        images_cartes['rouge_0']=pygame.image.load('images/cartes/rouge_0.jpg').convert_alpha()
        images_cartes['rouge_0']=pygame.transform.scale(images_cartes['rouge_0'],(lrg_carte,lng_carte))
        images_cartes['jaune_0']=pygame.image.load('images/cartes/jaune_0.jpg').convert_alpha()
        images_cartes['jaune_0']=pygame.transform.scale(images_cartes['jaune_0'],(lrg_carte,lng_carte))
        
        # Chargement des polices et d'images supplémentaires
        pol1 = pygame.font.SysFont('Bahnschrift',30,italic=True,bold=True)
        pol2 = pygame.font.SysFont('Bahnschrift',65,italic=True,bold=True)
        logo_carte = pygame.image.load('images/cartes/dos.jpg').convert_alpha()
        logo_carte = pygame.transform.scale(logo_carte,(lrg_carte*0.75, lng_carte*0.75))
        logo_uno = pygame.image.load('images/logo_uno.png').convert_alpha()
        logo_uno = pygame.transform.scale(logo_uno,(self.largeur / 3, self.hauteur / 3))
        
        if not self.jeu_commence: # Menu d'ouverture
            self.fenetre.fill((10, 120, 10))  # Fond vert

            # Dessiner le bouton "Jouer"
            pygame.draw.rect(self.fenetre, (255, 0, 0), self.bouton_jouer)
            police1 = pygame.font.Font(None, 36)
            police2 = pygame.font.SysFont('Bahnschrift',30,italic=True)
            txt_bouton = police1.render("Jouer", True, (255, 255, 255))
            self.fenetre.blit(txt_bouton, (self.bouton_jouer.x + 50, self.bouton_jouer.y + 10))
            
            # Afficher nom/prénom
            txt_nom = police2.render("Massinissa Bendahmane TG3", True, (255, 255, 255))
            self.fenetre.blit(txt_nom, (0, 0))
            
            # Afficher le logo "UNO"
            self.fenetre.blit(logo_uno,(self.largeur / 3, self.hauteur / 3 - 60))
            
        elif self.jeu_commence and not self.fin_jeu: # Pendant la partie
            self.fenetre.fill((10, 120, 10))  # Fond vert
            
            # Dessiner la pioche et la pile de cartes
            for i in range(5):
                self.fenetre.blit(images_cartes['dos'],(self.largeur / 2 - 1.5*lrg_carte, self.hauteur / 2 - lng_carte / 2 - (i+1)*6))
                if defausse.cartes[len(defausse.cartes)-5+i] == 'dos':
                    self.fenetre.blit(images_cartes['dos'],(self.largeur / 2 + 0.5*lrg_carte, self.hauteur / 2 - lng_carte / 2 - (i+1)*6))
                else:
                    self.fenetre.blit(images_cartes[str(defausse.cartes[len(defausse.cartes)-5+i].couleur+'_'+defausse.cartes[len(defausse.cartes)-5+i].valeur)],(self.largeur / 2 + 0.5*lrg_carte , self.hauteur / 2 - lng_carte / 2 - (i+1)*6))
            
            # Dessiner la main du joueur 1
            for i in range(len(main_joueur.cartes)):
                if len(main_joueur.cartes) <= 7:
                    self.fenetre.blit(images_cartes[str(main_joueur.cartes[i].couleur+'_'+main_joueur.cartes[i].valeur)],(170 + i*lrg_carte, self.hauteur - lng_carte))
                else:
                    distance = 560 / len(main_joueur.cartes) 
                    self.fenetre.blit(images_cartes[str(main_joueur.cartes[i].couleur+'_'+main_joueur.cartes[i].valeur)],(170 + i*distance, self.hauteur - lng_carte))
            
            # Dessiner la main de l'ordi
            for i in range(len(main_ordi.cartes)):
                if len(main_ordi.cartes) <= 7:
                    self.fenetre.blit(images_cartes['dos'],(170 + i*lrg_carte, 0))
                else:
                    distance = 560 / len(main_ordi.cartes) 
                    self.fenetre.blit(images_cartes['dos'],(170 + i*distance, 0))
                    
            # Afficher les cartes restantes
            # Pour l'ordi
            txt_cartes_ordi = pol1.render(str(len(main_ordi.cartes)), True, (255, 255, 255))
            self.fenetre.blit(txt_cartes_ordi, (self.largeur - 100, 20))
            self.fenetre.blit(logo_carte, (self.largeur - 110, 60))
            # Pour le joueur
            txt_cartes_joueur = pol1.render(str(len(main_joueur.cartes)), True, (255, 255, 255))
            self.fenetre.blit(logo_carte, (self.largeur - 110, self.hauteur - 150))
            self.fenetre.blit(txt_cartes_joueur, (self.largeur - 100, self.hauteur - 50))
            
            # Dessiner le profil du joueur
            txt_profil_joueur = pol1.render(joueur.nom, True, (255, 255, 255))
            logo_joueur = pygame.image.load('images/logo_joueur.png').convert_alpha()
            logo_joueur = pygame.transform.scale(logo_joueur,(120, 120))
            self.fenetre.blit(logo_joueur, (0, self.hauteur - 160))
            self.fenetre.blit(txt_profil_joueur, (0, self.hauteur - 40))
            
            # Dessiner le profil de l'ordi
            txt_profil_ordi = pol1.render(ordi.nom, True, (255, 255, 255))
            logo_ordi = pygame.image.load('images/logo_ordi.png').convert_alpha()
            logo_ordi = pygame.transform.scale(logo_ordi,(140, 140))
            self.fenetre.blit(txt_profil_ordi, (0, 10))
            self.fenetre.blit(logo_ordi, (0, 30))
            
            # Afficher le tour du joueur/de l'ordi
            if self.tour_joueur:
                txt_tour_actuel = pol1.render('À votre tour !', True, (255, 255, 255))
                self.fenetre.blit(txt_tour_actuel, (self.largeur / 2 - 100, self.hauteur / 2 + 120))
            else:
                txt_tour_actuel = pol1.render("Au tour de l'ordi !", True, (255, 255, 255))
                self.fenetre.blit(txt_tour_actuel, (self.largeur / 2 - 120, self.hauteur / 2 + 130))
            
            # Afficher le bouton UNO
            bouton_uno = pygame.image.load('images/logo_uno.png').convert_alpha()
            bouton_uno = pygame.transform.scale(bouton_uno,(self.largeur / 5, self.hauteur / 5))
            if self.tour_joueur and len(main_joueur.cartes) == 2 and not self.uno:
                self.fenetre.blit(bouton_uno, (0.8 * self.largeur, self.hauteur / 2 - 60))
            
            # Afficher la dernière action
            zone_action = pygame.Rect(30, 200, 250, 200)
            pygame.draw.rect(self.fenetre, (0, 50, 0), zone_action) # Fond de la zone d'affichage
            
            if self.tour_joueur: # Affichage de la dernière action de l'ordi
                txt_action = pol1.render("L'ordi a joué :", True, (255,255,255))
                self.fenetre.blit(txt_action, (zone_action.x, zone_action.y))
    
                if self.piocher:
                    self.fenetre.blit(images_cartes['dos'], (zone_action.x + 85, zone_action.y + 50))
                else:
                    if not self.tour_supplementaire_ordi:
                        if defausse.cartes[len(defausse.cartes)-1] in [bleu_0,rouge_0,vert_0,jaune_0]:
                            self.fenetre.blit(images_cartes[str(defausse.cartes[len(defausse.cartes)-2].couleur+'_'+defausse.cartes[len(defausse.cartes)-2].valeur)], (zone_action.x + 85, zone_action.y + 50))
                        else:
                            self.fenetre.blit(images_cartes[str(defausse.cartes[len(defausse.cartes)-1].couleur+'_'+defausse.cartes[len(defausse.cartes)-1].valeur)], (zone_action.x + 85, zone_action.y + 50))

            else: # Affichage de la dernière action du joueur
                txt_action = pol1.render("Vous avez joué :", True, (255,255,255))
                self.fenetre.blit(txt_action, (zone_action.x, zone_action.y))
                
                if self.piocher:
                    self.fenetre.blit(images_cartes['dos'], (zone_action.x + 85, zone_action.y + 50))
                else:
                    if not self.tour_supplementaire_ordi:
                        if defausse.cartes[len(defausse.cartes)-1] in [bleu_0,rouge_0,vert_0,jaune_0]: # Si un plus 4 ou un joker a été joué (pour éviter d'afficher la couleur uniquement)
                            self.fenetre.blit(images_cartes[str(defausse.cartes[len(defausse.cartes)-2].couleur+'_'+defausse.cartes[len(defausse.cartes)-2].valeur)], (zone_action.x + 85, zone_action.y + 50))
                        else:
                            self.fenetre.blit(images_cartes[str(defausse.cartes[len(defausse.cartes)-1].couleur+'_'+defausse.cartes[len(defausse.cartes)-1].valeur)], (zone_action.x + 85, zone_action.y + 50))

        elif self.fin_jeu: # Ecran de victoire/défaite
            self.fenetre.fill((10, 120, 10))  # Fond vert
            self.fenetre.blit(logo_uno,(self.largeur / 3, self.hauteur / 3 - 60))
            if len(main_joueur.cartes) == 0: # Si le joueur gagne
                txt_victoire = pol2.render('Vous remportez la victoire !', True, (255,255,255))
            else: # Si l'ordi gagne
                txt_victoire = pol2.render("L'ordi remporte la victoire...", True, (255,255,255))
            self.fenetre.blit(txt_victoire,(50,400))
            pygame.display.flip()
            pygame.time.wait(2600)
            self.en_cours = False
            
# Main

couleur=['rouge', 'vert', 'bleu', 'jaune','multicolore']
valeur=['1', '2', '3', '4', '5', '6', '7', '8', '9', 'interdit', 'inverse', 'plus2', 'plus4', 'couleur']
liste_cartes = jeu_50_cartes(couleur,valeur)
bleu_0 = Carte('0','bleu',False)
jaune_0 = Carte('0','jaune',False)
vert_0 = Carte('0','vert',False)
rouge_0 = Carte('0','rouge',False)
pioche=Paquet_de_Cartes(liste_cartes)
pioche.battre()
defausse=Paquet_de_Cartes([])
defausse.premiere_carte(pioche)
main_joueur,main_ordi = pioche.distribution(14)
joueur = Joueur('Joueur',main_joueur,0)
print("Ma main :")
main_joueur.affichage()
ordi = Joueur('Ordi',main_ordi,0)
print("Main de l'ordi :")
main_ordi.affichage()
print("Défausse :")
for i in range(len(defausse.cartes)):
    print(defausse.cartes[i])
lng_carte = 122
lrg_carte = 80

jeu = FenetreJeu(900, 600, "Uno simplifié")
jeu.lancer_jeu()

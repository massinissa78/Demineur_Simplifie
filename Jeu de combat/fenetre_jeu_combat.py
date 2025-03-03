# importation des bibliothèques

#------------------------------------------------------------------------------------------
import pygame
from pygame import *
from fonctions_jeu_combat import *
pygame.init()
#------------------------------------------------------------------------------------------

# création de la fenêtre de jeu

#------------------------------------------------------------------------------------------
fenetre = pygame.display.set_mode((900,600))
pygame.display.set_caption("Swordsman's Resolve")
fond = (0,0,0)
fenetre.fill(fond)
icone = pygame.image.load('images/icone.png').convert_alpha()
icone = pygame.display.set_icon(icone)
#------------------------------------------------------------------------------------------

# chargement des images du menu de démarrage

#------------------------------------------------------------------------------------------
bg_start = pygame.image.load('images/bg_menu.jpg').convert_alpha()
bg_start = pygame.transform.scale(bg_start,(996,600))
img_bouton_start = pygame.image.load('images/bouton_start.png').convert_alpha()
img_bouton_start = pygame.transform.scale(img_bouton_start,(320,140))
img_bouton_fight = pygame.image.load('images/bouton_fight.png').convert_alpha()
img_bouton_fight = pygame.transform.scale(img_bouton_fight,(270,118))
bandit_full = pygame.image.load('images/bandit_full.png').convert_alpha()
bandit_full = pygame.transform.scale(bandit_full,(564,800))
epeiste_full = pygame.image.load('images/epeiste_full.png').convert_alpha()
epeiste_full = pygame.transform.scale(epeiste_full,(532,800))
#------------------------------------------------------------------------------------------

# chargement des images de sélection des personnages

#------------------------------------------------------------------------------------------
bg_select = pygame.image.load('images/bg_select.jpg').convert_alpha()
bg_select = pygame.transform.scale(bg_select,(900,600))
port_1 = pygame.image.load(dictionnaire[1]['Nom_fichier']).convert_alpha()
port_1 = pygame.transform.scale(port_1,(120,120))
port_2 = pygame.image.load(dictionnaire[2]['Nom_fichier']).convert_alpha()
port_2 = pygame.transform.scale(port_2,(120,120))
port_3 = pygame.image.load(dictionnaire[3]['Nom_fichier']).convert_alpha()
port_3 = pygame.transform.scale(port_3,(120,120))
port_4 = pygame.image.load(dictionnaire[4]['Nom_fichier']).convert_alpha()
port_4 = pygame.transform.scale(port_4,(120,120))
port_5 = pygame.image.load(dictionnaire[5]['Nom_fichier']).convert_alpha()
port_5 = pygame.transform.scale(port_5,(120,120))
port_6 = pygame.image.load(dictionnaire[6]['Nom_fichier']).convert_alpha()
port_6 = pygame.transform.scale(port_6,(120,120))
port_7 = pygame.image.load(dictionnaire[7]['Nom_fichier']).convert_alpha()
port_7 = pygame.transform.scale(port_7,(120,120))
liste_images_perso = [port_1,port_2,port_3,port_4,port_5,port_6,port_7]
#------------------------------------------------------------------------------------------

# chargement des effets d'attaque magique et physique

#------------------------------------------------------------------------------------------
atq_mag = pygame.image.load('images/atq_mag.png').convert_alpha()
atq_mag = pygame.transform.scale(atq_mag,(275,200))
atq_phy = pygame.image.load('images/atq_phy.png').convert_alpha()
atq_phy = pygame.transform.scale(atq_phy,(275,200))
#------------------------------------------------------------------------------------------

# chargement des sprites des personnages en combat

#------------------------------------------------------------------------------------------
largeurs_sprites = [378,495,446,434,209,292,386]
sprite_1 = pygame.image.load(dictionnaire[1]['Nom_sprite']).convert_alpha()
sprite_1 = pygame.transform.scale(sprite_1,(378,440))
sprite_2 = pygame.image.load(dictionnaire[2]['Nom_sprite']).convert_alpha()
sprite_2 = pygame.transform.scale(sprite_2,(495,440))
sprite_3 = pygame.image.load(dictionnaire[3]['Nom_sprite']).convert_alpha()
sprite_3 = pygame.transform.scale(sprite_3,(446,440))
sprite_4 = pygame.image.load(dictionnaire[4]['Nom_sprite']).convert_alpha()
sprite_4 = pygame.transform.scale(sprite_4,(434,440))
sprite_5 = pygame.image.load(dictionnaire[5]['Nom_sprite']).convert_alpha()
sprite_5 = pygame.transform.scale(sprite_5,(209,440))
sprite_6 = pygame.image.load(dictionnaire[6]['Nom_sprite']).convert_alpha()
sprite_6 = pygame.transform.scale(sprite_6,(292,440))
sprite_7 = pygame.image.load(dictionnaire[7]['Nom_sprite']).convert_alpha()
sprite_7 = pygame.transform.scale(sprite_7,(386,440))
liste_sprites_perso = [sprite_1,sprite_2,sprite_3,sprite_4,sprite_5,sprite_6,sprite_7]
#------------------------------------------------------------------------------------------

# chargement des arrière-plans de combat

#------------------------------------------------------------------------------------------
bg_combat1 = pygame.image.load('images/bg_combat1.jpg').convert_alpha()
bg_combat1 = pygame.transform.scale(bg_combat1,(1066,600))
bg_combat2 = pygame.image.load('images/bg_combat2.jpg').convert_alpha()
bg_combat2 = pygame.transform.scale(bg_combat2,(1066,600))
bg_combat3 = pygame.image.load('images/bg_combat3.jpg').convert_alpha()
bg_combat3 = pygame.transform.scale(bg_combat3,(1066,600))
#------------------------------------------------------------------------------------------

# création du rectangle de sélection de perso

#------------------------------------------------------------------------------------------
rect_select = pygame.image.load('images/rect_select.png').convert_alpha()
rect_select = pygame.transform.scale(rect_select,(140,140))
pos_rect_select = rect_select.get_rect()
pos_rect_select = pos_rect_select.move(140,270)
#------------------------------------------------------------------------------------------

# création des polices d'écriture

#------------------------------------------------------------------------------------------
pol_menu = pygame.font.SysFont('Impact',86,italic=True)
pol_info_ordi = pygame.font.SysFont('Bahnschrift',75,italic=True)
pol_info = pygame.font.SysFont('Bahnschrift',50,italic=True)
pol_info2 = pygame.font.SysFont('Bahnschrift',40,italic=True)
pol_stats = pygame.font.SysFont('Bahnschrift',30,bold=True,italic=True)
pol_combat = pygame.font.SysFont('Bahnschrift',25,bold=True,italic=True)
pol_victoire = pygame.font.Font('pol_victoire.ttf',120)
pol_victoire.italic = True
#------------------------------------------------------------------------------------------

# chargement de la musique du menu et des effets sonores

#------------------------------------------------------------------------------------------
pygame.mixer.music.load('sons/menu.mp3')
pygame.mixer.music.set_volume(0.1)
dgt_phy = pygame.mixer.Sound('sons/dgt_physique.mp3')
dgt_phy.set_volume(0.1)
dgt_mag = pygame.mixer.Sound('sons/dgt_magique.ogg')
dgt_mag.set_volume(0.1)
#------------------------------------------------------------------------------------------

# main

#------------------------------------------------------------------------------------------
fenetre.blit(bg_start,(-48,0))
fenetre.blit(epeiste_full,(-20,150))
fenetre.blit(bandit_full,(400,150))
pygame.display.flip()
pygame.mixer.music.play(-1)
#------------------------------------------------------------------------------------------

# boucles du jeu

#------------------------------------------------------------------------------------------
jeu = 0 # le jeu est initialisé à la première phase : l'ouverture
persos_dispo = [0,1,2,3,4,5,6] # tous les personnages sont remis à disposition
while jeu < 11: #tant que le joueur n'a pas quitté le jeu (phase 11 = fin du jeu)
#------------------------------------------------------------------------------------------

    # boucle du menu de lancement
    
    #------------------------------------------------------------------------------------------
    if jeu == 0: # cette partie n'a lieu que lors du lancement du code
        start = False
        while not start:
            
            for event in pygame.event.get():
                
                # pour quitter le jeu en appuyant sur la croix
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    
                if event.type == pygame.KEYDOWN: # Attente des évènements au clavier
                    
                    if event.key == K_ESCAPE: # Quitter la boucle en appuyant sur Escape
                        pygame.display.flip()
                        pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN: # Attente de clic à la souris
                    
                    if event.button == 1: # Si clic gauche pressé
                        clic_x = event.pos[0]
                        clic_y = event.pos[1]
                        if 290 <= clic_x <= 610 and 400 <= clic_y <= 540: # Si le bouton start est pressé
                            start = True
                            jeu += 1
                            
            # actualisation de l'affichage
            titre_start = pol_menu.render("Swordsman's Resolve",True,(255,255,255))
            titre_start2 = pol_menu.render("Swordsman's Resolve",True,(0,0,0))
            fenetre.blit(titre_start2,(78,53))
            fenetre.blit(titre_start,(75,50))
            fenetre.blit(img_bouton_start,(290,400))
            pygame.display.flip()
    #------------------------------------------------------------------------------------------
            
    # phase de sélection du personnage par le joueur

    #------------------------------------------------------------------------------------------
    select_perso = False 
    perso_choisi = 0
    if jeu > 3: # remettre la musique du menu entre les combats
        pygame.mixer.music.load('sons/menu.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        
    while not select_perso: # tant que le joueur n'a pas choisi son perso
        
        for event in pygame.event.get():
            
            # pour quitter le jeu en appuyant sur la croix
            if event.type == pygame.QUIT:
                pygame.display.update()
                pygame.quit()
                
            if event.type == pygame.KEYDOWN: # Attente des évènements au clavier
                
                if event.key == K_ESCAPE: # Quitter la boucle en appuyant sur Escape
                    pygame.display.flip()
                    pygame.quit()
                
                # gestion du rectangle de sélection du personnage par le joueur
                if event.key == K_LEFT or event.key == K_q: # lorsque flèche de gauche ou Q appuyé/e
                    if 0 <= perso_choisi <= 3:
                        if perso_choisi > 0:
                            pos_rect_select = pos_rect_select.move(-160,0)
                            perso_choisi -= 1
                    if 4 <= perso_choisi <= 6:
                        if perso_choisi > 4:
                            pos_rect_select = pos_rect_select.move(-160,0)
                            perso_choisi -= 1
                            
                if event.key == K_RIGHT or event.key == K_d: # lorsque flèche de droite ou D appuyé/e
                    if 0 <= perso_choisi <= 3:
                        if perso_choisi < 3:
                            pos_rect_select = pos_rect_select.move(160,0)
                            perso_choisi += 1
                    if 4 <= perso_choisi <= 6:
                        if perso_choisi < 6:
                            pos_rect_select = pos_rect_select.move(160,0)
                            perso_choisi += 1
                            
                if event.key == K_DOWN or event.key == K_s: # lorsque flèche du bas ou S appuyé/e
                    if perso_choisi < 4:
                        if perso_choisi == 0:
                            pos_rect_select = pos_rect_select.move(0,160)
                            perso_choisi = 4
                        if perso_choisi == 1:
                            pos_rect_select = pos_rect_select.move(0,160)
                            perso_choisi = 5
                        if perso_choisi == 2:
                            pos_rect_select = pos_rect_select.move(0,160)
                            perso_choisi = 6
                        if perso_choisi == 3:
                            pos_rect_select = pos_rect_select.move(-160,160)
                            perso_choisi = 6
                            
                if event.key == K_UP or event.key == K_z: # lorsque flèche du haut ou Z appuyé/e
                    if perso_choisi > 3:
                        if perso_choisi == 4:
                            pos_rect_select = pos_rect_select.move(0,-160)
                            perso_choisi = 0
                        if perso_choisi == 5:
                            pos_rect_select = pos_rect_select.move(0,-160)
                            perso_choisi = 1
                        if perso_choisi == 6:
                            pos_rect_select = pos_rect_select.move(0,-160)
                            perso_choisi = 2
                            
            if event.type == pygame.MOUSEBUTTONDOWN: # valider la sélection en cliquant sur le bouton Fight
            
                if event.button == 1: # Si clic gauche pressé
                    clic_x = event.pos[0]
                    clic_y = event.pos[1]
                    if 600 <= clic_x <= 870 and 135 <= clic_y <= 253: # Si le bouton Fight est pressé
                        if perso_choisi in persos_dispo: # si le personnage choisi est disponible
                            select_perso = True
                            jeu += 1

        # récupération des infos du perso choisi
        img_perso_choisi = liste_images_perso[perso_choisi]
        nom_perso_choisi = pol_info.render(dictionnaire[perso_choisi+1]['Nom'],True,(0,0,0))
        classe_perso_choisi = pol_info2.render(("Classe : "+dictionnaire[perso_choisi+1]['Classe']),True,(0,0,0))
        perso_choisi_est_dispo = pol_info2.render("Perso indisponible !",True,(120,0,0))
                    
        # actualisation de l'affichage
        titre_select = pol_menu.render("Choisissez votre perso",True,(255,255,255))
        titre_select2 = pol_menu.render("Choisissez votre perso",True,(0,0,0))
        fenetre.blit(bg_select,(0,0))
        fenetre.blit(titre_select2,(53,12))
        fenetre.blit(titre_select,(50,9))
        fenetre.blit(port_1,(150,280))
        fenetre.blit(port_2,(310,280))
        fenetre.blit(port_3,(470,280))
        fenetre.blit(port_4,(630,280))
        fenetre.blit(port_5,(150,440))
        fenetre.blit(port_6,(310,440))
        fenetre.blit(port_7,(470,440))
        fenetre.blit(img_bouton_fight,(600,135))
        fenetre.blit(rect_select,pos_rect_select)
        fenetre.blit(img_perso_choisi,(90,125))
        fenetre.blit(nom_perso_choisi,(255,135))
        fenetre.blit(classe_perso_choisi,(255,185))
        if perso_choisi not in persos_dispo: # affiche un texte indiquant que ce perso est indisponible
            fenetre.blit(perso_choisi_est_dispo,(255,220))
        pygame.display.flip()
    #------------------------------------------------------------------------------------------
    
    # retrait du perso choisi de la liste des persos restants
        
    #------------------------------------------------------------------------------------------
    persos_dispo.remove(perso_choisi)
    pos_rect_select = rect_select.get_rect()
    pos_rect_select = pos_rect_select.move(140,270)
    #------------------------------------------------------------------------------------------

    # phase de sélection du personnage par l'ordinateur
    
    #------------------------------------------------------------------------------------------
    if select_perso == True: # le joueur doit avoir sélectionné son personnage pour que cette partie ait lieu

        # choix et affichage du personnage choisi par l'ordinateur et ses infos
        perso_choisi_ordi = choice(persos_dispo)

        while not perso_choisi_ordi in persos_dispo: # force l'ordi à choisir un perso différent et disponible
            perso_choisi_ordi = choice(persos_dispo)
        
        # récupération des infos du perso choisi par l'ordi      
        img_perso_choisi_ordi = pygame.image.load(dictionnaire[perso_choisi_ordi+1]['Nom_fichier']).convert_alpha()
        img_perso_choisi_ordi = pygame.transform.scale(img_perso_choisi_ordi,(360,360))
        nom_perso_choisi_ordi = pol_info_ordi.render(dictionnaire[perso_choisi_ordi+1]['Nom'],True,(0,0,0))
        classe_perso_choisi_ordi = pol_info_ordi.render(dictionnaire[perso_choisi_ordi+1]['Classe'],True,(0,0,0))

        # actualisation de l'affichage
        fenetre.blit(bg_select,(0,0))
        titre_select_ordi = pol_menu.render("L'ordinateur a choisi :",True,(255,255,255))
        titre_select2_ordi = pol_menu.render("L'ordinateur a choisi :",True,(0,0,0))
        fenetre.blit(titre_select2_ordi,(53,12))
        fenetre.blit(titre_select_ordi,(50,9))
        fenetre.blit(img_perso_choisi_ordi,(90,145))
        fenetre.blit(nom_perso_choisi_ordi,(500,155))
        fenetre.blit(classe_perso_choisi_ordi ,(500,230))
        pygame.display.flip()
        pygame.time.wait(2000)
    #------------------------------------------------------------------------------------------
    
    # retrait du perso choisi par l'ordi de la liste des persos restants
    
    #------------------------------------------------------------------------------------------
    persos_dispo.remove(perso_choisi_ordi)
    jeu += 1
    #------------------------------------------------------------------------------------------

    # phase de combat entre le joueur et l'ordi
    
    # initialisation des variables utilisées lors des tours de boucle
    
    #------------------------------------------------------------------------------------------
    combat = True
    if jeu == 3: # lors du 1er combat uniquement
        score_joueur = 0
        score_ordi = 0
    tour_act = 1
    debut_tour = True
    tour_attaque = False
    gagnant = {}
    perdant = {}
    fin_manche = False
    fin_combat = False
    type_atq = 0
    cote_atq = 0
    afficher_atq=False
    #------------------------------------------------------------------------------------------
    
    # chargement et lancement de la musique de combat
    
    #------------------------------------------------------------------------------------------
    pygame.mixer.music.load('sons/combat.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    #------------------------------------------------------------------------------------------

    # chargement des sprites de combat des personnages
    
    #------------------------------------------------------------------------------------------
    sprite_perso_choisi = liste_sprites_perso[perso_choisi]
    sprite_perso_choisi_ordi = liste_sprites_perso[perso_choisi_ordi]
    sprite_perso_choisi_ordi = pygame.transform.flip(sprite_perso_choisi_ordi,True,False)
    #------------------------------------------------------------------------------------------
    
    # copie des dicos des personnages pour le combat
    
    #------------------------------------------------------------------------------------------
    d_perso_joueur = selection_par_numero(perso_choisi+1,dictionnaire)
    d_perso_ordi = selection_par_numero(perso_choisi_ordi+1,dictionnaire)
    #------------------------------------------------------------------------------------------

    # gestion des barres de vie des personnages
    
    #------------------------------------------------------------------------------------------
    pv_act_joueur = int(d_perso_joueur['PV'])/int(dictionnaire[perso_choisi+1]['PV'])
    pv_manq_joueur = 1-pv_act_joueur
    pv_act_ordi = int(d_perso_ordi['PV'])/int(dictionnaire[perso_choisi_ordi+1]['PV'])
    pv_manq_ordi = 1-pv_act_ordi
    txt_pv_joueur = pol_stats.render(str(d_perso_joueur['PV']),True,(20,20,20))
    txt_pv_joueur2 = pol_stats.render(str(d_perso_joueur['PV']),True,(255,255,255))
    txt_pv_ordi = pol_stats.render(str(d_perso_ordi['PV']),True,(20,20,20))
    txt_pv_ordi2 = pol_stats.render(str(d_perso_ordi['PV']),True,(255,255,255))
    #------------------------------------------------------------------------------------------
    
    # création du texte du score
    
    #------------------------------------------------------------------------------------------
    txt_score = pol_stats.render((str(score_joueur)+" - "+str(score_ordi)),True,(20,20,20))
    #------------------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------------------
    while combat: # début de la boucle de combat

        for event in pygame.event.get():
            
            # pour quitter la boucle du jeu en appuyant sur la croix
            if event.type == pygame.QUIT:
                pygame.display.update()
                pygame.quit()
                
            if event.type == pygame.KEYDOWN: # Attente des évènements au clavier
                if event.key == K_ESCAPE: # Quitter la boucle en appuyant sur Escape
                    pygame.display.flip()
                    pygame.quit()
                    
        if fin_manche: # si l'un des 2 combattants est tombé K.O.
            if gagnant['Nom'] == d_perso_joueur['Nom']: # si le joueur a gagné
                # actualisation du texte de combat
                txt_combat = pol_combat.render(("Bravo ! Vous remportez la manche !"),True,(255,255,255))
                score_joueur += 1
            elif perdant['Nom'] == d_perso_joueur['Nom']: # si le joueur a perdu
                # actualisation du texte de combat
                txt_combat = pol_combat.render(("Dommage ! L'ordi remporte la manche..."),True,(255,255,255))
                score_ordi += 1
            afficher_atq = False
            fin_combat = True
            debut_tour = False
            tour_attaque = False
            jeu += 1
        
        #------------------------------------------------------------------------------------------
        if tour_attaque: # entame la séquence d'attaque pour 1 tour
            
            if ordre_attaque_ok and not fin_manche: # si l'ordre d'attaque a été choisi
                if ordre == 0: # si le premier personnage doit attaquer
                    attaquant,defenseur,dgt = attaque(attaquant,defenseur)
                    cote_atq = attaquant['Nom']
                    afficher_atq = True
                    # actualisation des barres de vie des personnages
                    if defenseur['Nom'] == d_perso_joueur['Nom']:
                        pv_act_joueur = int(defenseur['PV']) / int(dictionnaire[perso_choisi+1]['PV'])
                        pv_manq_joueur = 1 - pv_act_joueur
                        txt_pv_joueur = pol_stats.render(str(defenseur['PV']),True,(20,20,20))
                        txt_pv_joueur2 = pol_stats.render(str(defenseur['PV']),True,(255,255,255))
                    if defenseur['Nom'] == d_perso_ordi['Nom']:
                        pv_act_ordi = int(defenseur['PV']) / int(dictionnaire[perso_choisi_ordi+1]['PV'])
                        pv_manq_ordi = 1 - pv_act_ordi
                        txt_pv_ordi = pol_stats.render(str(defenseur['PV']),True,(20,20,20))
                        txt_pv_ordi2 = pol_stats.render(str(defenseur['PV']),True,(255,255,255))
                    # actualisation du texte de combat
                    txt_combat = pol_combat.render((attaquant['Nom']+" attaque et inflige "+str(dgt)+" dégâts !"),True,(255,255,255))
                    # actualisation de l'effet d'attaque
                    if attaquant['Classe'] == 'Physique':
                        type_atq = 1
                    if attaquant['Classe'] == 'Magique':
                        type_atq = 2
                    # vérification des PV restants du défenseur
                    if defenseur['PV'] == 0: # si le défenseur est K.O.
                        perdant = defenseur
                        gagnant = attaquant
                        fin_manche = True
                    
                if ordre == 1: # si le second personnage doit attaquer
                    defenseur,attaquant,dgt = attaque(defenseur,attaquant)
                    cote_atq = defenseur['Nom']
                    afficher_atq = True
                    # actualisation des barres de vie des personnages
                    if attaquant['Nom'] == d_perso_joueur['Nom']:
                        pv_act_joueur = int(attaquant['PV']) / int(dictionnaire[perso_choisi+1]['PV'])
                        pv_manq_joueur = 1 - pv_act_joueur
                        txt_pv_joueur = pol_stats.render(str(attaquant['PV']),True,(20,20,20))
                        txt_pv_joueur2 = pol_stats.render(str(attaquant['PV']),True,(255,255,255))
                    if attaquant['Nom'] == d_perso_ordi['Nom']:
                        pv_act_ordi = int(attaquant['PV']) / int(dictionnaire[perso_choisi_ordi+1]['PV'])
                        pv_manq_ordi = 1 - pv_act_ordi
                        txt_pv_ordi = pol_stats.render(str(attaquant['PV']),True,(20,20,20))
                        txt_pv_ordi2 = pol_stats.render(str(attaquant['PV']),True,(255,255,255))
                    # actualisation du texte de combat
                    txt_combat = pol_combat.render((defenseur['Nom']+" attaque et inflige "+str(dgt)+" dégâts !"),True,(255,255,255))
                    # actualisation de l'effet d'attaque
                    if defenseur['Classe'] == 'Physique':
                        type_atq = 1
                    if defenseur['Classe'] == 'Magique':
                        type_atq = 2
                    # vérification des PV restants du défenseur
                    if attaquant['PV'] == 0: # si le défenseur est K.O.
                        perdant = attaquant
                        gagnant = defenseur
                        fin_manche = True
                    # actualisation des variables
                    tour_act += 1
                    tour_attaque = False
                    
            # actualisation des variables
            if ordre_attaque_ok: # donner le tour à l'opposant après avoir attaqué ; n'est exécuté que si le combat a eu lieu
                if ordre == 0:
                    ordre = 1
                else:
                    ordre = 0
            
            if not ordre_attaque_ok: # si l'ordre d'attaque n'a pas été choisi
                attaquant,defenseur = ordre_attaque(d_perso_joueur,d_perso_ordi)
                # changement du texte de combat
                if attaquant == d_perso_joueur: # si le joueur commence
                    txt_combat = pol_combat.render(("Vous attaquez en premier !"),True,(255,255,255))
                else: # si l'ordi commence
                    txt_combat = pol_combat.render(("L'ordi attaque en premier !"),True,(255,255,255))
                ordre_attaque_ok = True
        #------------------------------------------------------------------------------------------
        
        #------------------------------------------------------------------------------------------
        if debut_tour: # marque le début du tour
            
            # changement du texte de combat
            txt_combat = pol_combat.render(("Tour n° "+str(tour_act)+" !"),True,(255,255,255))
            
            # actualisation des variables
            ordre_attaque_ok = False
            tour_attaque = True
            debut_tour = False
            ordre = 0
            afficher_atq = False

        if not debut_tour:
            if not tour_attaque: # si la séquence d'attaque est finie
                debut_tour = True
        #------------------------------------------------------------------------------------------
            
        # actualisation de l'affichage
        
        #------------------------------------------------------------------------------------------
        if jeu == 3: # à la 1ère manche
            fenetre.blit(bg_combat1,(-83,0))
        if jeu == 6: # à la 2nde manche
            fenetre.blit(bg_combat2,(-83,0))
        if jeu == 9: # à la 3ème manche
            fenetre.blit(bg_combat3,(-83,0))
        
        if not fin_manche:
            fenetre.blit(sprite_perso_choisi,(10,135))
            fenetre.blit(sprite_perso_choisi_ordi,(890 - largeurs_sprites[perso_choisi_ordi],135))
        if fin_manche:
            if gagnant['Nom'] == d_perso_joueur['Nom']: # si le joueur a gagné
                fenetre.blit(sprite_perso_choisi,(10,135))
            else: # si l'ordi a gagné
                fenetre.blit(sprite_perso_choisi_ordi,(890 - largeurs_sprites[perso_choisi_ordi],135))
                
        # affichage dynamique des barres de vie
        barre_pv_fond_joueur = pygame.draw.rect(fenetre,(30,30,30),(15,15,365,95))
        barre_pv_act_joueur = pygame.draw.rect(fenetre,(63,140,49),(30,30,335 * pv_act_joueur,65))
        barre_pv_manq_joueur = pygame.draw.rect(fenetre,(153,40,40),(30 + pv_act_joueur*335,30,335 * pv_manq_joueur,65))
        barre_vie_fond_ordi = pygame.draw.rect(fenetre,(30,30,30),(520,15,365,95))
        barre_vie_act_ordi = pygame.draw.rect(fenetre,(63,140,49),(535 + pv_manq_ordi*335,30,pv_act_ordi * 335,65))
        barre_pv_manq_ordi = pygame.draw.rect(fenetre,(153,40,40),(535,30,pv_manq_ordi * 335,65))
        
        # affichage du tableau des scores
        tableau_score_fond = pygame.draw.rect(fenetre,(30,30,30),(395,15,110,95))
        tableau_score = pygame.draw.rect(fenetre,(255,255,255),(410,30,80,65))
        
        # affichage de la zone de texte et des différents textes
        zone_txt = pygame.draw.rect(fenetre,(255,255,255),(15,480,870,105))
        zone_txt2 = pygame.draw.rect(fenetre,(0,0,0),(30,495,840,75))

        fenetre.blit(txt_pv_joueur,(40,49))
        fenetre.blit(txt_pv_joueur2,(38,47))
        fenetre.blit(txt_pv_ordi,(810,49))
        fenetre.blit(txt_pv_ordi2,(808,47))
        fenetre.blit(txt_score,(415,47))

        if afficher_atq: # si l'effet d'attaque doit être affiché
            
            if cote_atq == d_perso_joueur['Nom']: # si le joueur a attaqué
                if type_atq == 1: # lorsque attaque physique
                    atq_phy = pygame.image.load('images/atq_phy.png').convert_alpha()
                    atq_phy = pygame.transform.scale(atq_phy,(275,200))
                    fenetre.blit(atq_phy,(400,240))
                    pygame.mixer.Sound.play(dgt_phy)
                if type_atq == 2: # lorsque attaque magique
                    atq_mag = pygame.image.load('images/atq_mag.png').convert_alpha()
                    atq_mag = pygame.transform.scale(atq_mag,(275,200))
                    fenetre.blit(atq_mag,(400,240))
                    pygame.mixer.Sound.play(dgt_mag)
                    
            if cote_atq == d_perso_ordi['Nom']: # si l'ordinateur a attaqué
                if type_atq == 1: # lorsque attaque physique
                    atq_phy = pygame.image.load('images/atq_phy.png').convert_alpha()
                    atq_phy = pygame.transform.scale(atq_phy,(275,200))
                    atq_phy = pygame.transform.flip(atq_phy,True,False)
                    fenetre.blit(atq_phy,(225,240))
                    pygame.mixer.Sound.play(dgt_phy)
                if type_atq == 2: # lorsque attaque magique
                    atq_mag = pygame.image.load('images/atq_mag.png').convert_alpha()
                    atq_mag = pygame.transform.scale(atq_mag,(275,200))
                    atq_mag = pygame.transform.flip(atq_mag,True,False)
                    fenetre.blit(atq_mag,(225,240))
                    pygame.mixer.Sound.play(dgt_mag)

        fenetre.blit(txt_combat,(40,505))
        pygame.display.flip()
        pygame.time.wait(1600)

        if fin_combat:
            combat = False # fin de la boucle de combat
        #------------------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------------------
            
    # phase des résultats de la partie
    
    #------------------------------------------------------------------------------------------
    if jeu == 10: # attendre la fin des 3 manches
        
        if score_joueur > score_ordi: # si le joueur a gagné
            txt_victoire = pol_victoire.render('VICTOIRE !',True,(255,255,255))
            txt_victoire2 = pol_victoire.render('VICTOIRE !',True,(20,20,20))
            fenetre.blit(bg_combat3,(-83,0))
            fenetre.blit(txt_victoire2,(19,19))
            fenetre.blit(txt_victoire,(15,15))
            fenetre.blit(sprite_perso_choisi,(10,135))
            img_perso_choisi = pygame.image.load(dictionnaire[perso_choisi+1]['Nom_fichier']).convert_alpha()
            img_perso_choisi = pygame.transform.scale(img_perso_choisi,(350,350))
            fenetre.blit(img_perso_choisi,(475,180))
            pygame.display.flip()
            jeu += 1
            
        if score_joueur < score_ordi:
            txt_victoire = pol_victoire.render('DEFAITE...',True,(255,255,255))
            txt_victoire2 = pol_victoire.render('DEFAITE...',True,(20,20,20))
            fenetre.blit(bg_combat3,(-83,0))
            fenetre.blit(txt_victoire2,(19,19))
            fenetre.blit(txt_victoire,(15,15))
            fenetre.blit(sprite_perso_choisi_ordi,(890 - largeurs_sprites[perso_choisi_ordi],135))
            img_perso_choisi_ordi = pygame.image.load(dictionnaire[perso_choisi_ordi+1]['Nom_fichier']).convert_alpha()
            img_perso_choisi_ordi = pygame.transform.scale(img_perso_choisi_ordi,(350,350))
            fenetre.blit(img_perso_choisi_ordi,(75,180))
            pygame.display.flip()
            jeu += 1
        pygame.time.wait(4000)
    #------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
        
# fermeture de la fenêtre
        
#------------------------------------------------------------------------------------------
pygame.time.wait(2000)
pygame.display.update()
pygame.quit()
#------------------------------------------------------------------------------------------
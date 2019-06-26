#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *

from niveau import *
from joueur import *
from constantes import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre_x, cote_fenetre_y))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#interface joueur
interface_joueur = pygame.image.load(image_interface_joueur)

#Titre
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPALE
continuer = 1
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
			 	
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_F1:
					continuer_accueil = 0	#On quitte l'accueil
					choix = 'n1'		#On définit le niveau à charger
				#Lancement du niveau 2
				elif event.key == K_F2:
					continuer_accueil = 0
					choix = 'n2'
				elif event.key == K_F3:
					continuer_accueil = 0
					choix = 'n3'
		

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix,fond)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création du joueur
		local_player = Perso("images/dk_droite.png", "images/dk_gauche.png", 
		"images/dk_haut.png", "images/dk_bas.png", niveau, 10, 2 , 1)
			#Création du joueur
		local_player2 = Perso("images/en.png", "images/en.png", 
		"images/en.png", "images/en.png", niveau, 10, 2 , 1)

		liste_joueur = []
		liste_joueur.append(local_player)	
		liste_joueur.append(local_player2)	
		joueur_par_tour = len(liste_joueur) -1
		i = 0
	#BOUCLE DE JEU
	while continuer_jeu:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
	
			elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:

				niveau.evenemnt(liste_joueur[i],event, liste_joueur )

				if niveau.structure[liste_joueur[i].case_y][liste_joueur[i].case_x] == 'a':
					continuer_jeu = 0
				liste_joueur[i].combat(2) 
				i = i+1

				if joueur_par_tour < i: 
					i= 0
					joueur_par_tour = len(liste_joueur)-1
								#Victoire -> Retour à l'accueil
			
		for joueur in liste_joueur:
			if 	joueur.pv < 0:
				continuer_jeu = 0
		
		fenetre.blit(interface_joueur,(0,600))
		
		#fenetre.blit(box_surface_rect,0,0)
		niveau.Rafraichir(fenetre,liste_joueur,liste_joueur[i])
		#Affichages aux nouvelles positions
		#Afenetre.blit(fond, (0,0))
		#Aniveau.afficher(fenetre)
		#Abox_surface_rect = pygame.Surface((200, 200), pygame.SRCALPHA)
		#Afor joueur in liste_joueur:
		#A	fenetre.blit(joueur.direction, (joueur.x, joueur.y)) #joueur.direction = l'image dans la bonne direction
		#A	pygame.draw.rect(box_surface_rect, (255, 255, 255, 150), (joueur.x+1, joueur.y+1, 400,100))
		#A	fenetre.blit(box_surface_rect, (joueur.x+1,  joueur.y+1))
		#Apygame.display.flip()



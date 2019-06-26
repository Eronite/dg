#!/usr/bin/env python
  
# exemple barreprogression.py

import pygame
from pygame.locals import * 
from constantes import *
from niveau import *

# Fonction qui actualise la valeur de la barre de progression
# pour qu'on ait un petit peu de mouvement
def Barre_de_vie(fenetre,joueur):

	taux_de_vie = joueur.pv /joueur.pvmax
	taille_barre_de_vie =  taille_sprite_vie * taux_de_vie
	if taux_de_vie > 0.5:
		couleur = vert
	else:
		couleur = rouge

	pygame.draw.rect(fenetre, couleur, (14, 620, taille_barre_de_vie,31))

	text_to_blit = str(joueur.pv) +'/' + str(joueur.pvmax)
	font = pygame.font.Font(None, 24)
	text = font.render(text_to_blit ,1,(255,255,255)) 
	fenetre.blit(text, (50, 629))



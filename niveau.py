"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *
from math import *
from affichage import *
class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier,fond):
		self.fichier = fichier
		self.structure = 0
		self.fond	   = fond
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
	
	
	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			img_toblit = ''
			for sprite in ligne:
				if sprite == ';':
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if img_toblit == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif img_toblit == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif img_toblit == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					else:
						img = pygame.image.load("images/"+img_toblit+".png")
						fenetre.blit(img, (x,y))
					img_toblit = ''
					num_case += 1
				else:
				 img_toblit = img_toblit + sprite
			num_ligne += 1
	def Rafraichir(self, fenetre, listejoueur, joueur):
		Barre_de_vie(fenetre,joueur)
		#Affichages aux nouvelles positions
		fenetre.blit(self.fond, (0,0))
		self.afficher(fenetre)
		for joueur in listejoueur:
			fenetre.blit(joueur.direction, (joueur.x, joueur.y)) #joueur.direction = l'image dans la bonne direction

		pygame.display.flip()
			
	def collision(self, abscisse, ordonne, joueur, listejoueur):
		casex = floor(abscisse / taille_sprite) *taille_sprite
		casey = floor(ordonne / taille_sprite)  * taille_sprite
		for cible in listejoueur:
			if (casex == cible.x  and casey == cible.y) and (joueur != listejoueur ):
				cible.combat(joueur.attaque)

	def evenemnt( self, joueur, event,listejoueur):
		if event.type == KEYDOWN: 	
			#Si l'utilisateur presse Echap ici, on revient seulement au menu
			if event.key == K_ESCAPE:
				continuer_jeu = 0
				
			#Touches de déplacement 
			elif event.key == K_RIGHT:
				joueur.deplacer('droite')
			elif event.key == K_LEFT:
				joueur.deplacer('gauche')
			elif event.key == K_UP:
				joueur.deplacer('haut')
			elif event.key == K_DOWN:
				joueur.deplacer('bas')			
		elif  event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				#self.collision(event.pos[0],event.pos[1], joueur, listejoueur)
				joueur.deposer(event.pos[0],event.pos[1] )	   
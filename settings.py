import pygame
import os

# Taille écran
WIDTH = 800
HEIGHT = 900

# Couleurs 
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)  
VERT = (0,250,0)
JAUNE = (240,240,0)
BLEU = (0, 0, 255)

# Couleurs moins lumineuse
 
ROUGE_FONCE = (200, 0, 0)  
VERT_FONCE = (0,200,0)
BLEU_FONCE = (0, 0, 200)
JAUNE_FONCE = (220,220,0)

# Images
JOUEUR1 = pygame.image.load(os.path.join("images", "image-joueur1.png")) # image du joueur 1
JOUEUR2 = pygame.image.load(os.path.join("images", "image-joueur2.png")) # image du joueur 2

# Icon
ICON = pygame.image.load(os.path.join("images", "icon.jpg"))

# Background
MenuBG = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu.jpg")), (WIDTH, HEIGHT))
PAUSEBG = pygame.transform.scale(pygame.image.load(os.path.join("images", "pause.PNG")), (WIDTH, HEIGHT))
GameOverP1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "GameOverP1.png")), (WIDTH, HEIGHT))
GameOverP2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "GameOverP2.png")), (WIDTH, HEIGHT))
Instruction = pygame.transform.scale(pygame.image.load(os.path.join("images", "instructions.png")), (WIDTH, HEIGHT))
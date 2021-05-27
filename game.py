import pygame
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nom du jeu
pygame.display.set_caption("MegaJeu") 


# remplacement du  logo pygame par notre image
pygame.display.set_icon(ICON)

clock = pygame.time.Clock()

# relié à la fonction pause 
pause = False

# fonction text menu 
def text_objects(text, font):
    textSurface = font.render(text, True, BLANC)
    return textSurface, textSurface.get_rect()

# Fonction des paramètres des boutons
def button(msg,x,y,w,h,ic,ac,action=None):  # msg = message | x = disposition axe horizontal (width) | y = disposition axe vertical (height) | ia = couleur foncé | ac = couleur claire
    click = pygame.mouse.get_pressed() # mise en place du clic
    mouse = pygame.mouse.get_pos() # Recherche positionement de la souris
    
    # paramètre pour voir si la souris est dans l'espace du bouton
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #automatisation des boutons : paramètre msg, x,y,h,w,ac;ic à remplacer par les données voulues
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None: # Si la souris qui est sur un bouton enclenche le clic
            action()                         # alors l'action du bouton est enclenché
            #if action == "play":      --
                #play_game ()          ---
            #elif action == "quit":    -----> autre possibilité mais nécéssite d'ajouter une condition pour chaque bouton
                #pygame.quit()         ---

    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


# menu principal
def game_menu():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

        screen.blit(MenuBG, (0, 0)) # appel le background choisi pour le menu dans settings
        largeText=pygame.font.Font('freesansbold.ttf',50) # taille et police tu texte
        TextSurf, TextRect = text_objects("MegaJeu 1v1", largeText, ) # texte 
        TextRect.center = ((WIDTH/2),(HEIGHT/2)) #disposition du texte : ici au centre 
        screen.blit(TextSurf, TextRect) #apparition du texte sur l'écran
        button("Jouer",150,600,100,50,VERT_FONCE,VERT, play_game) # paramètre du bouton : son texte, sa position et taille, sa couleur et enfin l'action que celui-ci enclenche
        button("Quitter",550,600,100,50,ROUGE_FONCE,ROUGE, pygame.quit) # bouton quitter qui entraine l'action pygame.quit()
        button("Instructions",300,500,200,50,BLEU_FONCE,BLEU, instructions) #bouton Instruction qui a pour action de faire apparaitre la page action défini plus tard
        mouse = pygame.mouse.get_pos() # paramètre pour capter la souris

        pygame.display.update()
        clock.tick(15)




# Fonction de la page de pause 
def pause_():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
        #paramètre de l'ecran : couleur | Texte : couleur taille disposition et police 
        screen.blit(PAUSEBG, (0, 0))
        
        # Composé de deux boutons: continuer qui déclanche la fonction unpause
        button("Continuer",150,450,120,50,VERT_FONCE,VERT, unpause) #bouton qui suspend la pause et reprend le jeu là ou il a été laissé
        button("Stop",550,450,100,50,ROUGE_FONCE,ROUGE,pygame.quit) # déclenche la fin de partie avec pygame.quit()
        mouse = pygame.mouse.get_pos()
    
        pygame.display.update()
        clock.tick(15)

# reprise de jeu
def unpause():
    global pause
    pause = False #stop la pause

# page de fin de jeu
def gameOverP1():
    
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(GameOverP1, (0,0)) # image de fond
        
        button("Rejouer",150,100,100,50,VERT_FONCE,VERT,play_game) #bouton qui relance le jeu en faisant appel à la fonction de lancement de jeu
        button("Quitter",550,100,100,50,ROUGE_FONCE,ROUGE,pygame.quit)
        mouse = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(15)

def gameOverP2():
    
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(GameOverP2, (0,0)) # image de fond
        
        button("Rejouer",150,100,100,50,VERT_FONCE,VERT,play_game) #bouton qui relance le jeu en faisant appel à la fonction de lancement de jeu
        button("Quitter",550,100,100,50,ROUGE_FONCE,ROUGE,pygame.quit)
        mouse = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(15) 

def instructions():
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

        screen.blit(Instruction, (0,0)) # image de fond
        largeText=pygame.font.Font('freesansbold.ttf',50)  # Police et taille du texte
        TextSurf, TextRect = text_objects("Instructions", largeText, ) # Contenu du texte

        TextRect.center = ((WIDTH/2),80) # disposition centrée sur l'horizontal 
        screen.blit(TextSurf, TextRect) # Apparition du texte

        button("Quitter",50,50,100,50,ROUGE_FONCE,ROUGE, game_menu)# retourne sur le menu en faisant appel à sa fonction
        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(15)

# Mise en place du score en temps réel     
def drawScore():
        font = pygame.font.SysFont(None, 30) # police en 40
        text = font.render(f"Votre Score: {joueur.score}" , True, BLANC) # texte + appel du score 
        screen.blit(text,(600, 800)) # disposition en haut à droite
        text = font.render(f"Votre score: {joueur2.score}" , True, BLANC) # texte + appel du score 
        screen.blit(text,(600, 50)) # disposition en haut à droite

# Mise en place des condition du visuel de la vie : barre de vie de trois couleurs suivant l'evolution
def drawLivesP1():
        # conditions du visuel de la barre de vie ( rectangle en haut à gauche sur l'écran)
        if joueur.lives > 9:  # barre de vie longue et verte lorque les vies sont au max
            pygame.draw.rect(screen, VERT,(50,1, 70,20))
        elif joueur.lives > 4 : # diminution de la barre et changement de vie après une perte - changement de couleur et de la longueur (paramètre h fonction bouton)
            pygame.draw.rect(screen, JAUNE,(50,1, 40,20))
        else : # Barre de vie faible est rouge lorsqu'il reste très peu de vie
            pygame.draw.rect(screen, ROUGE,(50,1, 10,20))

def drawLivesP2():
        if joueur2.lives > 9:
            pygame.draw.rect(screen, VERT,(50,50, 70,20))
        elif joueur2.lives > 4 :
            pygame.draw.rect(screen, JAUNE,(50,50, 40,20))
        else :
            pygame.draw.rect(screen, ROUGE,(50,50, 10,20))

# Classe Joueur
class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = (JOUEUR1) # appel l'image du joueur
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2  #disposition du joueur au départ (largeur) - au millieu
        self.rect.centery = HEIGHT - 100 #disposition du joueur au départ (longueur)
        self.speedx = 0 # deplacement de la gauche vers la droite - immobile
        self.lives = 10 # nombre de vie accordées au joueur
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.score = 0

    # Déplacement Joueur avec flèches directionnelles GAUCHE et DROITE
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
   
    def tirs(self):
        balle = BalleP1(self.rect.centerx, self.rect.centery)
        all_sprites.add(balle)
        ballesp1.add(balle)

# Classe Joueur 2
class Joueur2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = (JOUEUR2) # appelle l'image du joueur
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2  #disposition du joueur au départ (largeur) - au millieu
        self.rect.centery = HEIGHT - 800 #disposition du joueur au départ (longueur)
        self.speedx = 0 # deplacement de la gauche vers la droite - immobile
        self.lives = 10 # nombre de vies accordées au joueur
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.score = 0

    # Déplacement Joueur avec flèches directionnelles GAUCHE et DROITE
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_q]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
   
    def tirs(self):
        balle = BalleP2(self.rect.centerx, self.rect.centery)
        all_sprites.add(balle)
        ballesp2.add(balle)

# Classe Balle (couleur, direction et vitesse tir)
class BalleP1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLEU) # appelle l'image de la balle
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = -10 #vitesse de déplacement du tir

    def update(self):
        self.rect.y += self.speedy

class BalleP2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(ROUGE) # appelle l'image de la balle
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = -10 #vitesse de déplacement du tir

    def update(self):
        self.rect.y -= self.speedy

all_sprites = pygame.sprite.Group()
ballesp1 = pygame.sprite.Group()
ballesp2 = pygame.sprite.Group()
joueur = Joueur()
joueur2 = Joueur2()
all_sprites.add(joueur, joueur2)

def play_game ():
# Jeu lancé
  
  jeu = True

  menu_display = True
  
  global pause

  while jeu:
    
    if menu_display:
        pygame.time.wait(3000)

        menu_display = False
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                joueur.tirs()
            elif event.key == pygame.K_e :
                joueur2.tirs()
    # Activation de l'écran pause par la touche p
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
             pause = True
             pause_()
    
    all_sprites.update()
    
    #Tir sur joueur p2 vers p1
    touchep1 = pygame.sprite.spritecollide(joueur, ballesp2, True)
    if touchep1:
        joueur2.score += 50
        joueur.score -= 15
        joueur.lives -= 1
    
    touchep2 = pygame.sprite.spritecollide(joueur2, ballesp1, True)
    if touchep2:
        joueur.score += 50
        joueur2.score -= 15
        joueur2.lives -= 1


    # Si le joueur n'a plus de vie le jeu se stop    
    if joueur.lives <= 0:
        gameOverP1()
    elif joueur2.lives <= 0 :
        gameOverP2()  # mise en place du menu game over lorsque le joueur a perdu toutes ses vies
    


    pygame.display.update()
    
    
    #Background
    screen.fill(NOIR)
    all_sprites.draw(screen)
    drawLivesP1()
    drawLivesP2()
    drawScore()
    pygame.display.flip()

game_menu()
play_game()
pygame.quit() 
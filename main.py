import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fener Arena")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#RENKLER
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#load backgorund image
bg_image = pygame.image.load("assets/images/background/Bootcamp-Arkaplan.jpg").convert_alpha()

# ARKAPLAN ÇİZME / DRAW BACKGROUND
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

# SAĞLIK BARI ÇİZME
def draw_health_bar(health, x ,y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 1, y - 1, 804, 54))
    pygame.draw.rect(screen, RED, (x, y, 800, 50))
    pygame.draw.rect(screen, YELLOW, (x, y, 800 * ratio, 50))

# KARAKTER OLUŞTUR
fighter_1 = Fighter(400, 620)
fighter_2 = Fighter(1400, 620)


#------------- OYUN DÖNGÜSÜ -------------

run = True
while run:

    clock.tick(FPS)
    # ARKAPLAN ÇİZ
    draw_bg()

    # OYUNCU STATLARI
    draw_health_bar(fighter_1.health, 50, 50)
    draw_health_bar(fighter_2.health, 1070, 50) 

    #karakterleri hareket ettir
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    #fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

    #karakterleri çiz
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update display
    pygame.display.update()

# pygameden çık
pygame.quit()

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Storing PNG as image
image = pygame.image.load('backgroundDino.png')

#Scaling image into background
def Background_Dino(image):
    size = pygame.transform.scale(image, (800, 600))
    screen.blit(size, (0, 0))

#Create window Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Create Player(rectangle)
player = pygame.Rect((300, 250, 50, 50))

#Keep running until user exits
run = True
while run:

    #Refreshes screen everytime player move(to not leave any pixels behind when moving)
    screen.fill((0, 0, 0))

    #Upload background
    Background_Dino(image)

    #Load Player(rectangle)
    pygame.draw.rect(screen, (255, 0, 0), player)

    #Player control (w,a,s,d)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    #If player exits then close screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
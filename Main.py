import random
import pygame

# Start pygame
pygame.init()

# Screen, gravity, and fps variables
screenWidth = 800
screenHeight = 600
jumpHeight = 15
gravity = 0.5
frames = 60

# Level of difficulty
difficulties = {
    "easy": 5,
    "medium": 10,
    "hard": 15,
    "impossible": 100
}

# Function to prompt user for difficulty
def userDifficulty():
    while True:
        level = input("Choose difficulty easy(5 blocks), medium(10 blocks), hard(15 blocks), impossible:")
        if level in difficulties:
            return level

# create Screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
image = pygame.image.load('backgroundDino.png')

#Function scales and displays image as background
def backgroundDino(image, bg_x):
    size = pygame.transform.scale(image, (800, 600))
    screen.blit(size, (bg_x, 0))


def generateObstacles(numObstacles):
    obstacles = []
    for x in range(numObstacles):
        rectWidth = random.randint(20, 100)
        rectHeight = 40
        # should create obstacles off-screen
        rectX = screenWidth + random.randint(100, 300)
        rectY = random.randint(0, screenHeight - rectHeight)
        rectSpeed = random.uniform(1, 4)
        #creates randomized obstacles with random size and speed
        obstacles.append((rectX, rectY, rectWidth, rectHeight, rectSpeed))
    return obstacles

bg_x = 0

# create player
player_width  = 50
player_height = 50
player = pygame.Rect(50, 250, player_width, player_height)

# Checking to see if obj is on the floor and is jumping
jumping = False
floor = True

# Variables to help player jump
y_velocity = jumpHeight
y_position = 365

# Used to control fps
clock = pygame.time.Clock()

# Prompt user for difficulty
difficulty = userDifficulty()

# Generate number of obstacles depending on difficulty level
num_obstacles = difficulties[difficulty]
obstacles = generateObstacles(num_obstacles)

# Game loop
run = True
while run:
    clock.tick(frames)

    # Background movement
    #bg_x -= 1

    # If the background moves out of the screen, reset its position
    #if bg_x <= 10:
     #   bg_x = 0

    # sets background
    backgroundDino(image, bg_x)

    # User Controls (a,d,space)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and player.left > 0:
        player.x -= 5
    elif key[pygame.K_d] and player.right < screenWidth:
        player.x += 5

    if key[pygame.K_SPACE] and floor:
        jumping = True
        y_velocity = jumpHeight
        floor = False

    if jumping:
        y_position -= y_velocity
        y_velocity -= gravity
        if y_position >= 365:
            y_position = 365
            jumping = False
            y_velocity = jumpHeight
            #Allows player to jump again when on the floor
            floor = True

    player.y = y_position

    # spawn player
    pygame.draw.rect(screen, (255, 0, 0), player)

    # spawn number of obstacles
    for x in range(len(obstacles)):
        rectX, rectY, rectWidth, rectHeight, rectSpeed = obstacles[x]
        rectX -= rectSpeed
        pygame.draw.rect(screen, (255, 255, 255), (rectX, rectY, rectWidth, rectHeight))
        obstacles[x] = (rectX, rectY, rectWidth, rectHeight, rectSpeed)  # Update obstacle position

        # checks for if player collided with obstacle
        if player.colliderect(pygame.Rect(rectX, rectY, rectWidth, rectHeight)):
            run = False
            break

        # checks if player has collided if so quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

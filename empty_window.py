import pygame

BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
<<<<<<< HEAD
ORANGE = (255,100,10)
=======




>>>>>>> 290031279541ae11225267dca8584b06361a07e4
offset = 0

o_1 = 700
o_2 = 720


speed = 100
pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)

x = 0 + offset
y = 425
width = 20
height = 25


pygame.display.set_caption("Dash n Jump")

clock = pygame.time.Clock()

isJump = False
jumpCount = 10



done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Game logic
    offset += 1
    o1 = o_1 - offset
    o2 = o_2 - offset

<<<<<<< HEAD
    if (offset > 700):
        offset = 0
           

    
    #Draw
    screen.fill(BLACK)
     
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 10)
    pygame.draw.rect(screen, RED, [350, 420, 20, 25], 5)
    pygame.draw.ellipse(screen, BLUE, [350, 420, 20, 25], 5)
    
    pygame.draw.polygon(screen, ORANGE,[[o1, 400], [o1 -10, 445], [o1 +10, 445]])
    pygame.draw.polygon(screen, ORANGE,[[o2, 400], [o2 -10, 445], [o2 +10, 445]])
=======
    if (offset > 790):
        offset = 790

    keys = pygame.key.get_pressed()

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False


    screen.fill(BLACK)
     
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 10)
    pygame.draw.rect(screen, RED, [0 + offset, y, 20, 25], 5) 
    pygame.draw.ellipse(screen, BLUE, [0 + offset, y, 20, 25], 5)
>>>>>>> 290031279541ae11225267dca8584b06361a07e4
    pygame.display.flip()
    
    clock.tick(speed)


pygame.quit()


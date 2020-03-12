import pygame

BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)




offset = 0

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
jumpCount = 7



done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Game logic
    offset += 1

    if (offset > 790):
        offset = 790

    keys = pygame.key.get_pressed()

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -7:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 7
            isJump = False


    screen.fill(BLACK)
     
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 10)
    pygame.draw.rect(screen, RED, [0 + offset, y, 20, 25], 5) 
    pygame.draw.ellipse(screen, BLUE, [0 + offset, y, 20, 25], 5)
    pygame.display.flip()

    clock.tick(60)


pygame.quit()


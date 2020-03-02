import pygame

BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 

pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

screen.fill(BLACK)

pygame.display.flip()

clock.tick(60)

pygame.quit()

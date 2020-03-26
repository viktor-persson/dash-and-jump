import pygame

BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255,100,10)

background = BLACK

offset = 0
obstacles_org = [700, 750, 900, 1000, 1050, 1200, 1300, 1350, 1500, 1600, 1700, 1750, 1850]

coldis = 30

speed = 100
pygame.init()
obstacles = obstacles_org.copy()
size = (800, 500)
screen = pygame.display.set_mode(size)


y = 420
height = 20

pygame.display.set_caption("Dash n Jump")

clock = pygame.time.Clock()

isJump = False
jumpCount = 7

done = False

def draw_obstacle_n_check(x_coord):
    pygame.draw.polygon(screen, ORANGE, [[x_coord, 400], [x_coord -25, 445], [x_coord + 25, 445]]) 
    if not isJump and abs(x_coord - 350) < coldis:
        return True
    else:
        return False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Game logic

    
    keys = pygame.key.get_pressed()

    v = 2

    if not(isJump):   
        if keys[pygame.K_SPACE]:
            isJump = True
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -7:
            y -= (jumpCount * abs(jumpCount)) * 0.1
            jumpCount -= 0.1
        else: 
            jumpCount = 7
            isJump = False

    


    for i in range(len(obstacles)):
        obstacles[i] -= 1
        if obstacles[i] < 0:
            obstacles[i] += 1300
        
    
    #Draw
    screen.fill(background)
     
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 10)
    pygame.draw.rect(screen, RED, [350, y, 20, 25], 5)
    pygame.draw.ellipse(screen, BLUE, [350, y, 20, 25], 5)
    
#    pygame.draw.polygon(screen, ORANGE,[[o1, 400], [o1 -10, 445], [o1 +10, 445]])
#    pygame.draw.polygon(screen, ORANGE,[[o2, 400], [o2 -10, 445], [o2 +10, 445]])

    for i in range(len(obstacles)):
        if draw_obstacle_n_check(obstacles[i]):
            background = RED
            
            

     

   
    

  
    

    pygame.display.flip()
    
    clock.tick(speed)


pygame.quit()


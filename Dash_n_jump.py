import pygame
import time
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255,100,10)

background = BLACK

offset = 0
obstacles_org = [700, 750, 900, 1000, 1050, 1200, 1300, 1350, 1500, 1650, 1700, 1700, 1850, 1900]

coldis = 30

score = 0
speed = 100
pygame.init()
obstacles = obstacles_org.copy()
size = (800, 500)
screen = pygame.display.set_mode(size)

x = 350
y = 420
height = 25
wide = 20
pygame.display.set_caption("Dash n Jump")

clock = pygame.time.Clock()

is_jump = False
isCrash = False
jumpCount = 7

done = False
pygame.mixer.music.load('MassiveEdge.wav')
pygame.mixer.music.play(-1)



def draw_obstacle_n_check(x_coord):
    pygame.draw.polygon(screen, ORANGE, [[x_coord, 400], [x_coord -25, 445], [x_coord + 25, 445]]) 
    if not is_jump and abs(x_coord - 350) < coldis:
        return True
    else:
        return False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Game logic

    
    keys = pygame.key.get_pressed()

    
        

      
    if keys[pygame.K_SPACE] and isCrash:
        score = 0
        isCrash = False
        background = BLACK
        pygame.mixer.music.play(-1)
        obstacles = obstacles_org.copy()
     
    if not(is_jump):        
        if keys[pygame.K_UP]:
            isJump = True
        
            
            is_jump = True
        elif keys[pygame.K_DOWN]:
            height = 15
            wide =25
            y = 430
        else: 
            height = 25
            wide = 20
            y = 420
    else:
        if jumpCount >= -7:
            y -= (jumpCount * abs(jumpCount)) * 0.1
            jumpCount -= 0.1
        else: 
            jumpCount = 7
            is_jump = False

    
    if not isCrash:
        for i in range(len(obstacles)):
            obstacles[i] -= 1
            if obstacles[i] < 0:
                obstacles[i] += 1300
        
    
    #Draw
    screen.fill(background)
     
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 10)
    pygame.draw.rect(screen, RED, [x, y, wide, height], 5) 
    
    

#    pygame.draw.polygon(screen, ORANGE,[[o1, 400], [o1 -10, 445], [o1 +10, 445]])
#    pygame.draw.polygon(screen, ORANGE,[[o2, 400], [o2 -10, 445], [o2 +10, 445]])

    for i in range(len(obstacles)):
        if draw_obstacle_n_check(obstacles[i]):
            background = RED
            pygame.mixer.music.stop()
            isCrash = True


    font1 = pygame.font.SysFont('Calibri', 75, True, False)
    font2 = pygame.font.SysFont('Calibri', 40, True, False)
    font3 = pygame.font.SysFont('Calibri', 15, True, False)
    font4 = pygame.font.SysFont('Calibri', 15, True, False)
    font5 = pygame.font.SysFont('Calibri', 15, True, False)
    font6 = pygame.font.SysFont('Calibri', 15, True, False)
    font7 = pygame.font.SysFont('Calibri', 15, True, False)
    font8 = pygame.font.SysFont('Calibri', 15, True, False)

    text1 = font1.render("LET'S JUMP", True, WHITE)
    text2 = font2.render(str(score) + " M", True, WHITE)
    text3 = font3.render("Press Keyup = Jump", True, WHITE)
    text4 = font4.render("Press Keydown = Dash", True, WHITE)
    text5 = font5.render("Press Space = Play Again", True, WHITE)
    text6 = font6.render("Press Keyup = Jump", True, BLACK)
    text7 = font7.render("Press Keydown = Dash", True, BLACK)
    text8 = font8.render("Press Space = Play Again", True, BLACK)
    
 
    screen.blit(text1, [200, 100])
    screen.blit(text2, [60, 30])
    screen.blit(text3, [20, 70])
    screen.blit(text4, [20, 87])
    screen.blit(text5, [20, 104])

    if score > 500:
        screen.blit(text6, [20, 70])
        screen.blit(text7, [20, 87])
        screen.blit(text8, [20, 104])        
    else: 
        screen.blit(text3, [20, 70])
        screen.blit(text4, [20, 87])
        screen.blit(text5, [20, 104])
       

    

    pygame.display.flip()
    if not isCrash:
        score += 1
        
    clock.tick(speed)

pygame.quit()

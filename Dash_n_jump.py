import pygame
import time
import copy
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255,100,10)

background = BLACK
ob_h = 325
ob_l = 345


offset = 0
obstacles_org = [[700, ob_l], [750, ob_l], [900,ob_h], [1000,ob_l], [1050,ob_l], [1200,ob_h], [1300,ob_l], [1350,ob_l], [1500,ob_l], [1650,ob_l], [1700,ob_l] , [1850,ob_h], [1900,ob_h]]
obstacles = []
coldis = 30

score = 0
speed = 100
pygame.init()
obstacles = copy.deepcopy(obstacles_org)
size = (800, 500)
screen = pygame.display.set_mode(size)

x = 350
y = 420
height = 25
wide = 20
pygame.display.set_caption("Dash n Jump")

clock = pygame.time.Clock()

is_jump = False
is_dash = False
isCrash = False
jumpCount = 7
font_color = WHITE

done = False
pygame.mixer.music.load('MassiveEdge.wav')
pygame.mixer.music.play(-1)



def draw_obstacle_n_check(coord):
    pygame.draw.polygon(screen, ORANGE, [[coord[0], coord[1]], [coord[0] -25, coord[1] + 100], [coord[0] + 25, coord[1] + 100]]) 
    if not is_jump and abs(coord[0] - 350) < coldis and coord[1] == ob_l :
        return True
    elif not is_dash and abs(coord[0] - 350) < coldis and coord[1] == ob_h:
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
        obstacles = copy.deepcopy(obstacles_org)
    
     
    if not(is_jump):        
        if keys[pygame.K_UP]:
            isJump = True
            is_jump = True
        
        elif keys[pygame.K_DOWN]:
            height = 15
            wide =25
            y = 430
            is_dash = True
        else: 
            height = 25
            wide = 20
            y = 420
            is_dash = False

    else:
        if jumpCount >= -7:
            y -= (jumpCount * abs(jumpCount)) * 0.1
            jumpCount -= 0.1
        else: 
            jumpCount = 7
            is_jump = False

    
    if not isCrash:
        for i in range(len(obstacles)):
            obstacles[i][0] -= 1
            if obstacles[i][0] < 0:
                obstacles[i][0] += 1300
        
    
    #Draw
    screen.fill(background)
     
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 10)
    pygame.draw.rect(screen, RED, [x, y, wide, height], 5) 
    

    for i in range(len(obstacles)):
        if draw_obstacle_n_check(obstacles[i]):
            background = RED
            pygame.mixer.music.stop()
            isCrash = True


    font75 = pygame.font.SysFont('Calibri', 75, True, False)
    font40 = pygame.font.SysFont('Calibri', 40, True, False)
    font15 = pygame.font.SysFont('Calibri', 15, True, False)

    text1 = font75.render("LET'S JUMP", True, WHITE)
    text2 = font40.render(str(score) + " M", True, WHITE)
    text3 = font15.render("Press Keyup = Jump", True, font_color)
    text4 = font15.render("Press Keydown = Dash", True, font_color)
    text5 = font15.render("Press Space = Play Again", True, font_color)    
 
    screen.blit(text1, [200, 100])
    screen.blit(text2, [60, 30])
    
    if score > 500:
        font_color = BLACK
    else:
        font_color = WHITE
        
    screen.blit(text3, [20, 70])
    screen.blit(text4, [20, 87])
    screen.blit(text5, [20, 104])
       

    

    pygame.display.flip()
    if not isCrash:
        score += 1
        
    clock.tick(speed)

pygame.quit()

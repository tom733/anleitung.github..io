import pygame 
 
x = 500
y = 500 
 
title = "Pong" 
 
run = True 
 
pygame.init()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption(title) 

while run: 
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:    
                    run = False   
        pygame.display.flip() 
racketWidth = 100
racketHeight = 15 
 
racketX = 200
racketY = 450 
 
... 
 
pygame.draw.rect(screen, (255, 40, 0), (racketX, racketY, racketWidth, racketHeight), 0)
speed = 0 
 
... 
 
def moveRacket():  
    global racketX  
    racketX += speed 
 
 
def racketBlock():  
    global speed  
    if racketX <= 0 or racketX >= x - racketWidth:   
        speed = 0 
                
... 
                
                if event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_LEFT:    
                        speed = -2  
                        if event.key == pygame.K_RIGHT:     
                        speed = 2   
    screen.fill((0, 0, 0)) 
    moveRacket()  
    racketBlock() 
 
... 
ballX = int(x/2)
ballY = int(y/2) 
 
ballRadius = 15 
 
... 
 
pygame.draw.circle(screen, (255, 255, 0), (ballX, ballY), ballRadius, 0) 
 
... 
def ballBlock():  
    global ballYSpeed, ballXSpeed  
    if ballY - ballRadius <= 0:      
        ballYSpeed *= -1  
    if ballX - ballRadius <= 0:    
        ballXSpeed *= -1  
    if ballX + ballRadius >= x:    
        ballXSpeed *= -1  
    if ballY >= 435 and ballY <= 440:    
        if ballX >= racketX -15 and ballX <= racketX + racketWidth + 15:     
            ballYSpeed *= -1 
ballXSpeed = 1
ballYSpeed = -2 
 
... g
 
def moveBall():  
    global ballX, ballY  
    ballX += ballXSpeed  
    ballY += ballYSpeed 
 
... 
 
moveBall()
ballBlock() 
 
...
import random 
 
... 
 
def reset():  
    global ballYSpeed, ballXSpeed, life, ballX, ballY, racketX, racketY, speed   
    racketX = 200  
    racketY = 450 
 
 
    ballX = int(x/2)  
    ballY = int(y/2) 
 
    speed = 0  
    ballXSpeed = random.randint(-2, 2)  
    if ballXSpeed == 0:    
        ballXSpeed = 1   
    ballYSpeed = -2  
    screen.fill((0, 0, 0))  
    pygame.draw.circle(screen, (255, 255, 0), (ballX, ballY), ballRadius, 0)  
    pygame.draw.rect(screen, (255, 40, 0), (racketX, racketY, racketWidth, racketHeight), 0)  
    pygame.display.flip()  
    pygame.time.wait(1000)
pygame.quit()
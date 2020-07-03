import pygame 
pygame.init() 


win = pygame.display.set_mode((500, 500)) # Dies erzeugt ein Fenster von 500 Breite und 500 Höhe. 
pygame.display.set_caption("First Game") 
x = 50 
y = 50
width = 40 
height = 60
vel = 5 

isJump = False
jumpCount = 10 
 
run = True 
 
while run: 
    pygame.time.delay(1)# Dadurch wird das Spiel um die angegebene Anzahl von Millisekunden verzögert. In unserem Fall werden 0,1 Sekunden die Verzögerung sein. 
    
    for event in pygame.event.get():  # Dabei wird eine Liste mit beliebigen Tastatur- oder Mausereignissen durchlaufen. 
        if event.type == pygame.QUIT: # Überprüft, ob die rote Schaltfläche in der Ecke des Fensters angeklickt wurde      
            run = False # Beendet die Spielschleife 
 
 
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))  # Diese nimmt: Fenster/Oberfläche, Farbe, Rechteck-Informationen 
    pygame.display.update() # Dies aktualisiert das Fenster, so dass wir unser Rechteck sehen können.     
    keys = pygame.key.get_pressed()  # Dadurch erhalten wir einen Array, in dem jede Taste einen Wert von 1 oder 0 hat, wobei 1 gedrückt und 0 nicht gedrückt ist. 
 
    if keys[pygame.K_LEFT] and x > vel: # So können wir prüfen, ob eine Taste gedrückt wird 
         x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
         x += vel
    if not (isJump): # Prüft, ob der Benutzer nicht springt 
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height- vel: 
            y += vel
        if keys[pygame.K_SPACE]: 
            isJump = True
    else:
        # Das wird passieren, wenn wir springen
        if jumpCount >= -10:      
            y -= (jumpCount * abs(jumpCount)) * 0.5     
            jumpCount -= 1 
        else: # Dies wird ausgeführt, wenn der Sprung beendet ist
            jumpCount = 10  
            isJump = False   
            # Zurücksetzen unserer Variablen 

    win.fill((0,0,0))  # Füllt den Hintergrund mit Schwarz  
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))  
    pygame.display.update()   
         
pygame.quit()
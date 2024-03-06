import pygame 
import sys



class Game: #Classen einbauen wird einfacher zu erwitern 
    def __init__(self): 
        pygame.init() 
        self.screen = pygame.display.set_mode((800, 600)) # screen große einsetzten 
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Balls") #Name fon programm 
        self.background_img = pygame.image.load('data/images/clouds/cloud_1.png') # Bild auswählen 
        self.background_img.set_colorkey((0,0,0)) # die ausgewelten farbe wird durchsichtig // 0,0,0 ist schwarz
        self.background_img_pos = [180,250]
        self.background_img_movement =[False,False]


    def run(self): #Funktion zum rufen 
        while True: #einfach wie Loop das die spiele Funktion 
            
            self.screen.fill((14,186,250)) # hier wird den hintergrund farbe gesetzt 
            self.background_img_pos[1] += (self.background_img_movement[1] - self.background_img_movement[0])*5 # boolen werden in int um gewandelt so dass di ekeiden knopf gedrukt wirden, es wird sich nix bewegen 
            self.screen.blit(self.background_img, self.background_img_pos) #

            for event in pygame.event.get(): # mit dem können wir den programm zum laufen bringen ohne das windows es schließt 
                if event.type == pygame.QUIT: # hier wir den "x" von spiel funktion gergeben 
                    pygame.quit() # mit dem wird nur pygame geschloßen 
                    sys.exit()  # mit dem wird windows den programm schließen 
                
                if event.type == pygame.KEYDOWN: # Wenn der knopf gedrukt wird // fallender Flanke 
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.background_img_movement[0] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.background_img_movement[1] = True
                if event.type == pygame.KEYUP: # Wenn der knopf los gelassen wird // steigneder Flanke
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.background_img_movement[0] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.background_img_movement[1] = False


            pygame.display.update() #das ist für programm zu zeigen 
            self.clock.tick(60)	# das ist um FPS fix zu stellen 

Game().run()
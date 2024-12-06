import pygame
import math

class Weapon():
    def __init__(self, image):
        self.imageOriginal = image
        self.angulo = 0
        self.image = pygame.transform.rotate(self.imageOriginal, self.angulo)
        self.forma = self.image.get_rect()

    def update(self, player):
        self.forma.center = player.forma.center
        if player.flip == False:
            self.forma.x += player.forma.width/2.7
            self.rotarArma(False)

        if player.flip == True:
            self.forma.x -= player.forma.width / 2.7
            self.rotarArma(True)

        self.forma.y -= player.forma.height/7.9
        mousePos = pygame.mouse.get_pos()
        diferenciaX = mousePos[0] + self.forma.centerx
        diferenciaY = (mousePos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(diferenciaY, diferenciaX))



    def dibujar(self, interfaz):
        self.image = pygame.transform.rotate(self.image, self.angulo)
        interfaz.blit(self.image, self.forma)

    def rotarArma(self, rotar):
        if rotar == True:
            imagenFlip = pygame.transform.flip(self.imageOriginal, True, False)
            self.image = pygame.transform.rotate(imagenFlip, self.angulo)
        else:
            imagenFlip = pygame.transform.flip(self.imageOriginal, False, False)
            self.image = pygame.transform.rotate(imagenFlip, self.angulo)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,image,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.imageOriginal = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.imageOriginal, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


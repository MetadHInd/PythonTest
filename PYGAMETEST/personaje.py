import pygame
import constantes
import weapon

class Personaje():

    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        self.frameIndex= 0
        self.image = animaciones[self.frameIndex]
        self.updateTime = pygame.time.get_ticks()
        self.forma = self.image.get_rect()
        self.forma.center = (x,y)

    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        self.forma.x += delta_x
        self.forma.y += delta_y

    def update(self):
        cooldownAnimacion = 80
        self.image = self.animaciones[self.frameIndex]
        if pygame.time.get_ticks() - self.updateTime >= cooldownAnimacion:
            self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()
        if self.frameIndex >= len(self.animaciones):
            self.frameIndex = 0

    def draw(self, interfaz):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(image_flip, self.forma)


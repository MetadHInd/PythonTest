from operator import truediv
import pygame
import constantes
from personaje import Personaje
from weapon import Weapon



from constantes import ANCHO_VENTANA, ALTO_VENTANA

pygame.init()

def escalarImg(image):
    player_img = pygame.transform.scale(image, (
    image.get_width() * constantes.SCALA_PERSONAJE, image.get_height() * constantes.SCALA_PERSONAJE))
    return player_img

animaciones = []
for i in range(7):
    img = pygame.image.load(f"assets//images//character//player//{i+1}.png")
    img = escalarImg(img)
    animaciones.append(img)

imagen_pistola = pygame.image.load("assets//images//weapons//GUN_01_[square_frame]_01_V1.00.png")
imagen_pistola = escalarImg(imagen_pistola)
imagen_bala = pygame.image.load("assets//images//weapons//bala.png")
imagen_bala = escalarImg(imagen_bala)

window = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('primer juego')
player = Personaje(60, 60, animaciones)

pistola = Weapon(imagen_pistola)

#Variable movimiento player
moverArriba = False
moverAbajo = False
moverDerecha = False
moverIzquierda = False
reloj = pygame.time.Clock()
run = True

while run:

    reloj.tick(constantes.FPS)
    window.fill(constantes.COLOR_FONDO)

    #Calcular movimiento player
    delta_x = 0
    delta_y = 0

    if moverDerecha == True:
        delta_x = 4
    if moverIzquierda == True:
        delta_x = -4
    if moverArriba == True:
        delta_y = -4
    if moverAbajo == True:
        delta_y = 4

    player.movimiento(delta_x, delta_y)
    player.update()
    pistola.update(player)
    player.draw(window)
    pistola.dibujar(window)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moverIzquierda = True

            if event.key == pygame.K_d:
                moverDerecha = True

            if event.key == pygame.K_w:
                moverArriba = True

            if event.key == pygame.K_s:
                moverAbajo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moverIzquierda = False

            if event.key == pygame.K_d:
                moverDerecha = False

            if event.key == pygame.K_w:
                moverArriba = False

            if event.key == pygame.K_s:
                moverAbajo = False
    pygame.display.update()

pygame.quit()
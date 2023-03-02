import pygame
from pygame import mixer

pygame.init()
mixer.init()

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Need For Speed UnderPython")
pos_carro_x = 363
pos_carro_y = 350

pos_carro_vermelho_x = 360
pos_carro_vermelho_y = -400

pos_carro_amarelo_x = 470
pos_carro_amarelo_y = -200

pos_carro_cinza_x = 250
pos_carro_cinza_y = 50
velocidade = 10
distancia = 10
janela_aberta = True

mixer.music.load("./sound/trilha.mp3")
mixer.music.set_volume(0.5)
#mixer.music.play()

fundo = pygame.image.load("./img/fundo.png")
icon = pygame.image.load("./img/icon.png")
carro = pygame.image.load("./img/carro.png")
carro_vermelho = pygame.image.load("./img/carro_vermelho.png")
carro_amarelo = pygame.image.load("./img/carro_amarelo.png")
carro_cinza = pygame.image.load("./img/carro_cinza.png")

fundo = pygame.transform.scale(fundo, (800, 600))
carro = pygame.transform.scale(carro, (80, 165))
carro_vermelho = pygame.transform.scale(carro_vermelho, (80, 165))
carro_amarelo = pygame.transform.scale(carro_amarelo, (80, 165))
carro_cinza = pygame.transform.scale(carro_cinza, (80, 165))

pygame.display.set_icon(icon)

while(janela_aberta):
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        pos_carro_y -= distancia
    if comandos[pygame.K_DOWN]:
        pos_carro_y += distancia
    if comandos[pygame.K_RIGHT]:
        pos_carro_x += distancia
    if comandos[pygame.K_LEFT]:
        pos_carro_x -= distancia

    pos_carro_cinza_y += velocidade
    if pos_carro_cinza_y > 600:
        pos_carro_cinza_y = -200
    pos_carro_amarelo_y += velocidade
    if pos_carro_amarelo_y > 600:
        pos_carro_amarelo_y = -500
    pos_carro_vermelho_y += velocidade
    if pos_carro_vermelho_y > 600:
        pos_carro_vermelho_y = -400

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (pos_carro_x, pos_carro_y))
    janela.blit(carro_vermelho, (pos_carro_vermelho_x, pos_carro_vermelho_y))
    janela.blit(carro_cinza, (pos_carro_cinza_x, pos_carro_cinza_y))
    janela.blit(carro_amarelo, (pos_carro_amarelo_x, pos_carro_amarelo_y))

    pygame.display.update()

pygame.quit()

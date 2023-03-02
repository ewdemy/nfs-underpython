import pygame
from pygame import mixer
from random import randint

pygame.init()
mixer.init()

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Need For Speed UnderPython")
pos_carro_x = 373
pos_carro_y = 350

pos_carro_vermelho_x = 372
pos_carro_vermelho_y = -400

pos_carro_amarelo_x = 483
pos_carro_amarelo_y = -200

pos_carro_cinza_x = 258
pos_carro_cinza_y = 50
distancia = 15
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
tamanho_carro = (60, 130)
fundo = pygame.transform.scale(fundo, (800, 600))
carro = pygame.transform.scale(carro, tamanho_carro)
carro_vermelho = pygame.transform.scale(carro_vermelho, tamanho_carro)
carro_amarelo = pygame.transform.scale(carro_amarelo, tamanho_carro)
carro_cinza = pygame.transform.scale(carro_cinza, tamanho_carro)

pygame.display.set_icon(icon)

while(janela_aberta):
    velocidade = randint(5, 25)
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT]:
        pos_carro_x += distancia
    if comandos[pygame.K_LEFT]:
        pos_carro_x -= distancia

    pos_carro_cinza_y += velocidade + 5
    if pos_carro_cinza_y > 600:
        pos_carro_cinza_y = randint(-1500, -200)
    pos_carro_amarelo_y += velocidade + 10
    if pos_carro_amarelo_y > 600:
        pos_carro_amarelo_y = randint(-1500, -500)
    pos_carro_vermelho_y += velocidade
    if pos_carro_vermelho_y > 600:
        pos_carro_vermelho_y = randint(-1500, -400)

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (pos_carro_x, pos_carro_y))
    janela.blit(carro_vermelho, (pos_carro_vermelho_x, pos_carro_vermelho_y))
    janela.blit(carro_cinza, (pos_carro_cinza_x, pos_carro_cinza_y))
    janela.blit(carro_amarelo, (pos_carro_amarelo_x, pos_carro_amarelo_y))

    pygame.display.update()

pygame.quit()

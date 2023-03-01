import pygame
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Need For Speed UnderPython")
x = 350
y = 200

distancia = 10
janela_aberta = True

fundo = pygame.image.load("./img/fundo.png")
carro_vermelho = pygame.image.load("./img/carro_vermelho.png")
carro_amarelo = pygame.image.load("./img/carro_amarelo.png")

fundo = pygame.transform.scale(fundo, (800,600))
carro_vermelho = pygame.transform.scale(carro_vermelho, (100,180))

while(janela_aberta):
    pygame.time.delay(50)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            janela_aberta = False

        comandos = pygame.key.get_pressed()
    if(comandos[pygame.K_UP]):
        y-= distancia
    if (comandos[pygame.K_DOWN]):
        y += distancia
    if (comandos[pygame.K_RIGHT]):
        x += distancia
    if (comandos[pygame.K_LEFT]):
        x -= distancia

    janela.blit(fundo,(0,0))
    janela.blit(carro_vermelho,(x,y))


    pygame.display.update()


pygame.quit()
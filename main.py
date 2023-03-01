import pygame
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Need For Speed UnderPython")
x = 400
y = 300

distancia = 10
janela_aberta = True
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

    janela.fill((0,0,0))
    pygame.draw.circle(janela, (0,255,0), (x,y), 50)
    pygame.display.update()


pygame.quit()
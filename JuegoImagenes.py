import pygame
pygame.init()
font = pygame.font.Font('freesansbold.ttf',24)
screen = pygame.display.set_mode([800,500])
timer = pygame.time.Clock()
mensajes = ["mensaje1","mensaje2"]
counter = 0
speed = 3
active_message = 0
message = mensajes[active_message]
done = False
run = True
pictures = {}
rutas_imagenes = ['imagen1.png','imagen2.png']

for i in rutas_imagenes:
    picture = pygame.image.load('Images\\'+i)
    picture = pygame.transform.scale(picture, (800, 380))
    picture_rect = picture.get_rect(topleft=(0, 0))
    pictures[picture] = picture_rect
screen.fill('white')
screen.blit(list(pictures)[active_message], list(pictures.values())[active_message])
while run:
    timer.tick(60)
    pygame.draw.rect(screen,'black',[0,380,800,120])
    if counter < speed *len(message):
        counter += 1
    elif counter >= speed*len(message):
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_message<len(mensajes)-1:
                active_message +=1
                done =False
                message = mensajes[active_message]
                counter = 0
                screen.blit(list(pictures)[active_message], list(pictures.values())[active_message])
                pygame.display.update()
    snip = font.render(message[0:counter//speed],True,'white')
    screen.blit(snip,(10,420))
    pygame.display.flip()
pygame.quit()

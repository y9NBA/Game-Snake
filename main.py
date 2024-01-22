import pygame

pygame.init()
game_ending = False
fps = pygame.time.Clock()

dis = pygame.display.set_mode((600,600))
pygame.display.set_gamma(20,20,20)
x, y = 200, 200
x1, y1 = 0, 0
pygame.display.set_caption("Game Snake", "Snake")

def snakebody():
    

while not game_ending:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ending = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                x1 = 0
                y1 = 10
            elif event.key == pygame.K_UP:
                x1 = 0
                y1 = -10
            elif event.key == pygame.K_LEFT:
                x1 = -10
                y1 = 0
            elif event.key == pygame.K_RIGHT:
                x1 = 10
                y1 = 0

    if x <= 0:
        x = 600
    elif x >= 600:
        x = 0
    if y <= 0:
        y = 600
    elif y >= 600:
        y = 0

    x += x1
    y += y1

    snakebody()
    pygame.display.update()

    dis.fill((255, 255, 255))
    fps.tick(60)

pygame.quit()
quit()

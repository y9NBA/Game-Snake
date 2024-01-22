import pygame

pygame.init()
dis = pygame.display.set_mode((600,600))
pygame.display.set_caption("Game Snake", "Snake")

def snakebody(snakebody_list: list) -> None:
    for x in snakebody_list:
        pygame.draw.rect(dis,(20,20,20), [x[0],x[1],10,10])

def loop() -> None:

    x, y = 200, 200
    x1, y1 = 0, 0
    game_ending = False
    speed = pygame.time.Clock()
    speed_value = 30
    snakebody_list = []
    length_snakebody = 1

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
                if event.key == pygame.K_ESCAPE:
                    game_ending = True

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

        dis.fill((255, 255, 255))

        snakehead = []

        snakehead.append(x)
        snakehead.append(y)
        snakebody_list.append(snakehead)

        if len(snakebody_list) > length_snakebody:
            del snakebody_list[:-1]

        #game_ending = True if len([x for x in snakebody_list[:-1] if x == snakehead]) == 1 else False
        for x in snakebody_list[:-1]:
            if x == snakehead:
                game_ending = True

        snakebody(snakebody_list)
        pygame.display.update()

        speed.tick(speed_value)

    pygame.quit()
    quit()


loop()

import pygame

pygame.init()
dis = pygame.display.set_mode((600,600))
pygame.display.set_caption("Game Snake", "Snake")

def snakebody(block: int,snakebody_list: list) -> None:
    for x in snakebody_list:
        pygame.draw.rect(dis,(20,20,20), [x[0],x[1],block,block])

def message(msg, row, column = 1, fontsize = 20) -> None:
    mesg = pygame.font.SysFont("Arial", fontsize).render(msg, True, (255,0,0))
    dis.blit(mesg, [100 * column, 100 * row])

def loop() -> None:

    x, y = 300, 300
    x1, y1 = 0, 0
    block = 10

    game_ending = False
    game_over = False

    speed = pygame.time.Clock()
    speed_value = block * 3

    snakebody_list = []
    length_snakebody = 1

    while not game_ending:
        while game_over == True:
            dis.fill((0, 0, 90))
            message("Игра окончена!", 2, 2, 26)
            message("Чтобы начать заново, нажмите R, для выхода нажмите Esc.", 3)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_ending = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = False
                        game_ending = True
                    if event.key == pygame.K_r:
                        loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_ending = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    x1 = 0
                    y1 = block
                elif event.key == pygame.K_UP:
                    x1 = 0
                    y1 = -block
                elif event.key == pygame.K_LEFT:
                    x1 = -block
                    y1 = 0
                elif event.key == pygame.K_RIGHT:
                    x1 = block
                    y1 = 0
                if event.key == pygame.K_ESCAPE:
                    game_ending = True
                if event.key == pygame.K_r:
                    loop()

        if x >= 600 or x <= 0 or y >= 600 or y <= 0:
            game_over = True
        #if x <= 0:
        #    x = 600
        #elif x >= 600:
        #    x = 0
        #if y <= 0:
        #    y = 600
        #elif y >= 600:
        #    y = 0

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
            if x == snakehead and x != snakebody_list[0]:
                game_over = True

        snakebody(block, snakebody_list)
        pygame.display.update()

        speed.tick(speed_value)

    pygame.quit()
    quit()


if __name__ == "__main__":
    loop()

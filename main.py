import pygame
import random

pygame.init()
dis = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Game Snake", "Snake")

def snakebody(block: int, snakebody_list: list) -> None:
    '''
    Отображение всего тела змейки
    :param block:
    :param snakebody_list:
    :return:
    '''
    for i in snakebody_list:
        pygame.draw.rect(dis,(20,20,20), [i[0],i[1],block,block])

def message(msg, row, column = 1, fontsize = 20) -> None:
    mesg = pygame.font.SysFont("Arial", fontsize).render(msg, True, (255,0,0))
    dis.blit(mesg, [100 * column, 100 * row])

def food(coordinate: list, block: int) -> None:
    '''
    Генератор еды
    :param coordinate:
    :param block:
    :return:
    '''
    pygame.draw.rect(dis, (255, 0, 0), [coordinate[0], coordinate[1], block, block])

def loop() -> None:
    '''
    Главная логика игры
    :return:
    '''

    x, y = 300, 300
    x1, y1 = 0, 0
    block = 10

    game_ending = False
    game_over = False
    isFood = True

    speed = pygame.time.Clock()
    speed_value = block

    snakebody_list = []
    length_snakebody = 1
    food_xy = [random.randint(10, x - 10) // 10 * 10, random.randint(10, y - 10) // 10 * 10]

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

        # if x >= 600 or x <= 0 or y >= 600 or y <= 0: #Условие для ограниченного поля
        #   game_over = True

        #Условие для безграничного поля
        if x <= 0:
            x = 600
        elif x >= 600:
            x = 0
        if y <= 0:
            y = 600
        elif y >= 600:
            y = 0

        x += x1 #Смещение по оси x
        y += y1 #Смещение по оси y

        dis.fill((255, 255, 255)) #Обновление доски

        food(food_xy, block) #Генерирует еду

        snakehead = []
        snakehead.append(x)
        snakehead.append(y)
        snakebody_list.append(snakehead)

        if len(snakebody_list) > length_snakebody: #Не позволяет хаотично расти и растягиваться змейке
            del snakebody_list[0]

        #game_ending = True if len([x for x in snakebody_list[:-1] if x == snakehead]) == 1 else False

        for i in snakebody_list[:-1]: #Смерть в случае столкновения с самим собой
            if i == snakehead:
                game_over = True

        if not isFood:
            food_xy = [random.randint(0, 600) // 10 * 10, random.randint(0, 600) // 10 * 10]
            isFood = True

        if x == food_xy[0] and y == food_xy[1]:
            length_snakebody += 1
            speed_value += 1
            isFood = False

        snakebody(block, snakebody_list)
        pygame.display.update()

        speed.tick(speed_value)

    pygame.quit()
    quit()


if __name__ == "__main__":
    loop()

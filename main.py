from metods.generators import *
from metods.game_metods import *

import pygame

pygame.init()
width, height = 600, 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Snake", "Snake")

def start() -> None:
    '''
    Что то типо главного меню перед началом самой игры
    :return:
    '''
    
    game_start = False
    while not game_start:
        dis.fill((90,90,60))
        message(dis, "Для начала игры нажмите Space", 5, 3, 26)
        message(dis, "Для выхода нажмите Esc", 8, 4, 20)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_SPACE:
                        game_start = True
                        loop(50, 3)
                    case pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

def loop(block: int, speed_value: int) -> None:
    '''
    Главная логика игры
    :return:
    '''

    x, y = width // 2, height // 2
    x1, y1 = 0, 0

    game_ending = False
    game_over = False
    isFood = True

    speed = pygame.time.Clock()
    score = 0

    snakebody_list = []
    length_snakebody = 1
    food_xy = random_coord(width, height, block)

    while not game_ending:
        while game_over:
            dis.fill((0, 0, 90))
            message(dis, "Игра окончена!", 4, 4, 26)
            message(dis, "Чтобы начать заново, нажмите R, для выхода нажмите Esc.", 6)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_ending = True
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            game_over = False
                            game_ending = True
                            start()
                        case pygame.K_r:
                            loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_ending = True
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_DOWN | pygame.K_s:
                        x1, y1 = 0, block
                    case pygame.K_UP | pygame.K_w:
                        x1, y1 = 0, -block
                    case pygame.K_LEFT | pygame.K_a:
                        x1, y1 = -block, 0
                    case pygame.K_RIGHT | pygame.K_d:
                        x1, y1 = block, 0
                    case pygame.K_ESCAPE:
                        game_ending = True
                        start()
                    case pygame.K_r:
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

        dis.fill((255, 255, 255)) #Переворот доски с новыми изменениями, выход на новый кадр

        food(dis, food_xy, block) #Генерирует еду

        snakehead = [x,y]
        snakebody_list.append(snakehead)

        if len(snakebody_list) > length_snakebody: #Не позволяет хаотично расти и растягиваться змейке
            del snakebody_list[0]

        #game_over = True if len([i for i in snakebody_list[:-1] if i == snakehead]) == 1 else False

        for i in snakebody_list[:-1]: #Смерть в случае столкновения с самим собой
            if i == snakehead:
                game_over = True

        if not isFood:
            food_xy = random_coord(width, height, block)
            isFood = True

        if x == food_xy[0] and y == food_xy[1]:
            length_snakebody += 1
            score += 1
            isFood = False
            if score % 5 == 0:
                speed_value += 1

        snakebody(dis, block, snakebody_list)
        pygame.display.update() #Обновление доски

        speed.tick(speed_value)

    pygame.quit()
    quit()
    

if __name__ == "__main__":
    start()
    
import pygame


def snakebody(display: pygame.Surface, block: int, snakebody_list: list) -> None:
    """
    Отображение/отрисовка всего тела змейки
    :param display:
    :param block:
    :param snakebody_list:
    :return:
    """

    for i in snakebody_list:
        pygame.draw.rect(display, (20, 20, 20), [i[0], i[1], block, block])


def message(display: pygame.Surface, msg: str, row: int=0, column: int=1, fontsize=20, color=(255, 255, 255)) -> None:
    """
    Вывод сообщения на экран
    :param display:
    :param msg:
    :param row:
    :param column:
    :param fontsize:
    :param color:
    :return:
    """

    mesg = pygame.font.SysFont("Arial", fontsize).render(msg, True, color)
    display.blit(mesg, [50 * column, 50 * row])

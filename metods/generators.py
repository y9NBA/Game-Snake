import pygame
import random

def food(display: pygame.Surface, coordinate: list, block: int) -> None:
    '''
    Генератор еды
    :param coordinate:
    :param block:
    :return:
    '''

    pygame.draw.rect(display, (255, 0, 0), [coordinate[0], coordinate[1], block, block])

def random_coord(width: int, height: int, block: int, margin: int = 10) -> list:
    '''
    Генератор случайных координат
    :param width:
    :param height:
    :param block:
    :param margin:
    :return list:
    '''

    return [random.randint(margin, width - margin) // block * block, random.randint(margin, height - margin) // block * block]
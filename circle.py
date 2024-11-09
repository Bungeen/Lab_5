import math


def area(r):
    '''Принимает число r, возвращает квадрат числа r 
    помноженный на число Пи из библиотеки math: площадь круга'''
    if r > 0:
        return math.pi * r * r
    return 0


def perimeter(r):
    '''Принимает число r, возвращает удвоенное 
    произведение чила r на Пи из библиотеки math: периметр круга'''
    if r > 0:
        return 2 * math.pi * r
    return 0


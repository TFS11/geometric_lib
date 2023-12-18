import math


def area(r):
    '''
    Принимает значение r,
    возвращает произведение Пи на квадрат r
    '''
    if type(r) not in [int, float]:
        raise TypeError('radius must be an integer')
    if r<0:
        raise ValueError("radians negative")
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает значение r,
    возвращает удвоенное произведение Пи на r
    '''
    if type(r) not in [int, float]:
        raise TypeError('radius must be an integer')
    if r<0:
        raise ValueError("radians negative")
    return 2 * math.pi * r

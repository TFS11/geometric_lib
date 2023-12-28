import math


def area(r):
    '''
    Принимает значение радиуса круга, возвращает его площадь
    Пример: input:5 output:78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает значение радиуса круга, возвращает его периметр
    Пример: input:5 output:31.41592653589793
    '''
    return 2 * math.pi * r
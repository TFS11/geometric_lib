
def area(a):
    '''
    Принимает число a,
    возвращает квадрат числа a
    '''
    if type(a) not in [int, float]:
        raise TypeError('values must be an integer')
    if a<0:
        raise ValueError("values negative")
    return a * a


def perimeter(a):
    '''
    Принимает число a,
    возвращает произведение 4 и a
    '''
    if type(a) not in [int, float]:
        raise TypeError('values must be an integer')
    if a<0:
        raise ValueError("values negative")
    return 4 * a

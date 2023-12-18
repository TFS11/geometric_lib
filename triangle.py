def area(a, h):
    '''
    Принимает числа a и h,
    возвращает значение половины от произведения a и h
    '''
    if type(a) not in [int, float] or type(h) not in [int, float]:
        raise TypeError('values must be an integer')
    if a<0 or h<0:
        raise ValueError("values negative")
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Принимает числа a, b и c,
    возвращает сумму a, b и c
    '''
    if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
        raise TypeError('values must be an integer')
    if a<0 or b<0 or c<0:
        raise ValueError("values negative")
    return a + b + c 

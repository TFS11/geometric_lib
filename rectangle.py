def area(a, b):
    '''
    Принимает значения a и b,
    возвращает произведение a и b
    '''
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('values must be an integer')
    if a<0 or b<0:
        raise ValueError("values negative")
    return a * b 

def perimeter(a, b):
    '''
    Принимает значения a и b,
    возвращает удвоенную сумму a и b
    '''
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('values must be an integer')
    if a<0 or b<0:
        raise ValueError("values negative")
    return (a + b)*2


def area(a):
    '''Принимает число a, возвращает произведение квадрата числа a на коэффициент 3 * sqrt(3) / 2'''
    if a > 0:
        return 3 ** 1.5 / 2 * a ** 2
    return 0

def perimeter(a): 
    '''Принимает число a, возвращает 6 * a'''
    if a > 0:
        return 6 * a
    return 0

def mainDiagonal(a):
    '''Принимает число a, возвращает удвоенное a'''
    if a > 0:
        return 2 * a
    return 0

def subDiagonal(a):
    '''Принимает число a, возвращает sqrt(3) * a'''
    if a > 0:
        return 3 ** 0.5 * a
    return 0

import math

def area(r):
    """
    Возвращает площадь круга радиуса r.
    Параметры:
        r (float | int): радиус круга (r >= 0).
    Возвращает:
        float: площадь круга (π * r^2).
    Пример:
        round(area(3), 2)
        28.27

        area(0)
        0.0
    """
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает длину окружности (периметр круга) радиуса r.
    Параметры:
        r (float | int): радиус круга (r >= 0).
    Возвращает:
        float: длина окружности (2 * π * r).
    Пример:
        round(perimeter(3), 2)
        18.85
        perimeter(0)
        0.0
    """
    return 2 * math.pi * r

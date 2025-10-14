def area(width, height):
    """
    Возвращает площадь прямоугольника со сторонами width и height.
    Параметры:
        width (float | int): длина стороны по ширине (width >= 0).
        height (float | int): длина стороны по высоте (height >= 0).
    Возвращает:
        float: площадь прямоугольника (width * height).
    Пример:
        area(3, 4)
        12.0

        round(area(2.5, 7), 2)
        17.5
    """
    return float(width) * float(height)


def perimeter(width, height):
    """
    Возвращает периметр прямоугольника со сторонами width и height.
    Параметры:
        width (float | int): длина стороны по ширине (width >= 0).
        height (float | int): длина стороны по высоте (height >= 0).
    Возвращает:
        float: периметр прямоугольника (2 * (width + height)).
    Пример:
        perimeter(3, 4)
        14.0

        round(perimeter(2.5, 7), 2)
        19.0
    """
    return 2.0 * (float(width) + float(height))

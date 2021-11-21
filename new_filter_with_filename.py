from PIL import Image
import numpy as np

def get_grayscale(i, width, width_mosaic, j, height, height_mosaic, gray, matrix):
    """
    Функция, возвращающая степень оттенков серых
    :param width: ширина самого рисунка
    :param width_mosaic: ширина мозаики
    :param height: высота самого рисунка
    :param height_mosaic: высота мозаики
    :param gray: степень оттенков серых
    :param matrix: мозаика
    :return: возвращает степень оттенков серых
    >>> get_grayscale(0, 110, 100, 0, 110, 100, 5, [[[100, 110, 120]]])
    1
    """

    for cur_width in range(i, min(i + width // width_mosaic, width)):
        for cur_height in range(j, min(j + height // height_mosaic, height)):
            red = matrix[cur_width][cur_height][0]
            green = matrix[cur_width][cur_height][1]
            blue = matrix[cur_width][cur_height][2]
            gray += (int(red) + int(green) + int(blue)) / 3
    return int(gray // 100)


def create_grey_picture(x, width, width_mosaic, y, height, height_mosaic, grayscale_step, grayscale, matrix):
    """
    Функция, возвращающая картинку в степени оттенка серого
    :param width: ширина самой картинки
    :param width_mosaic: ширина мозаики
    :param height: высота самой картинки
    :param height_mosaic: высота мозаики
    :param grayscale_step: шаг градации серого
    :param grayscale: оттенок серого
    :return: картинка в степени оттенка серого
    >>> create_grey_picture(0, 110, 100, 0, 110, 100, 10, 512, [[[100, 110, 120]]])
    [[[50000, 50000, 50000]]]
    """
    for cur_width in range(x, min(x + width // width_mosaic, width)):
        for cur_height in range(y, min(y + height // height_mosaic, height)):
            matrix[cur_width][cur_height] = [int(grayscale // 50 * grayscale_step) * grayscale_step * 50] * 3
    return matrix


img = Image.open("rtf.jpg")
matrix = np.array(img)
width = len(matrix)
height = len(matrix[1])

width_mosaic = 10
height_mosaic = 10
grayscale_step = 50

i = 0
while i < width - 1:
    j = 0
    while j < height - 1:
        grayscale = get_grayscale(i, width, width_mosaic, j, height, height_mosaic, grayscale_step, matrix)
        matrix = create_grey_picture(i, width, width_mosaic, j, height, height_mosaic, grayscale_step,
                                     grayscale, matrix)
        j = j + height // height_mosaic
    i = i + width // width_mosaic
res = Image.fromarray(matrix)
res.save('res.jpg')

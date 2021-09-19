# Данный модуль содержит функции работы с подсчётом количества необходимых пикселей
from PIL import Image
SOURCE_DIR = 'static/uploads/'


def rgb2hex(r, g, b): # Перевод из RGB в HEX формат
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex_to_rgb(hex_string): # Перевод из HEX в RGB формат
    r_hex = hex_string[1:3]
    g_hex = hex_string[3:5]
    b_hex = hex_string[5:7]
    return int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)


def Count_Pixel(hex_code, file_name): # Функция подсчёта количества пикселей необходимого цвета. hex_code - HEX-код
    # цвета пикселя, file_name - имя файла
    file_path = Image.open(SOURCE_DIR + file_name)
    black = 0
    white = 0
    color = 0
    for pixel in file_path.getdata():
        if pixel == (0, 0, 0):
            black += 1
        if pixel == (255, 255, 255):
            white += 1
    if black > white:
        message = 'Чёрных пикселей больше'
    elif black < white:
        message = 'Белых пикселей больше'
    else:
        message = 'Чёрных и белых пиеселей одинаковое количество'
    q2 = hex_to_rgb(hex_code)
    for pixel in file_path.getdata():
        if pixel == q2:
            color += 1
    return black, white, color, message


def color_input_validation(input_color): # Проверка введённого пользователем HEX-кода на правильность
    if input_color == "":
        return False # Введено пустое ничего не введено
    if input_color[0] != '#':
        return False # 'Первый символ должен быть решёткой'
    if len(input_color) != 7:
        return False # 'Неверное количество символов'
    try:
        int(input_color[1:], 16)
        return True
    except:
        return False # Число введено неверно

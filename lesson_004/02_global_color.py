# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

point_triangle = sd.get_point(100, 150)
point_squad = sd.get_point(600, 150)
point_pentagon = sd.get_point(100, 400)
point_hexagon = sd.get_point(600, 400)


def triangle(point, angle, length, color):
    new_point = point
    for angle in range(angle + 0, angle + 361, 120):
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw(color=color)
        new_point = v.end_point


def square(point, angle, length, color):
    new_point = point
    for angle in range(angle + 0, angle + 361, 90):
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw(color=color)
        new_point = v.end_point


def pentagon(point, angle, length, color):
    new_point = point
    for angle in range(angle + 0, angle + 361, 72):
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw(color=color)
        new_point = v.end_point


def hexagon(point, angle, length, color):
    new_point = point
    for angle in range(angle + 0, angle + 361, 60):
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw(color=color)
        new_point = v.end_point


# TODO, предлагаю объединить словарь и список в один массив.
#  Ключём будет ввод пользователя в текстовом формате, а значением список из названия цвета и функции =)
color_figure = {
    0: ("red", sd.COLOR_RED),
    1: ("orange", sd.COLOR_ORANGE),
    2: ("yellow", sd.COLOR_YELLOW),
    3: ("green", sd.COLOR_GREEN),
    4: ("cyan", sd.COLOR_YELLOW),
    5: ("blue", sd.COLOR_BLUE),
    6: ("purple", sd.COLOR_PURPLE)
}

# TODO, для запроса корректного ввода пользователя, предлагаю реализовать цикл while True.
#  Если ввод пользователя есть в словаре, создаём переменную с цветом и выходим из цикла =)
#  Проверить наличие ключа в словаре можно при помощи "in" =)

print('Возможные цвета:')

for key, value in color_figure.items():
    print(key, ':', value[0])

while True:                 # Прошу объяснить зачем надо делать бесконечный цикл, программа же и без него работает
    number = input()
    number = int(number)

    if number in color_figure.keys():
        color = color_figure.get(number)[1]
    else:
        print('Введите корректный номер')

    triangle(point=point_triangle, angle=0, length=100, color=color)
    square(point=point_squad, angle=0, length=100, color=color)
    pentagon(point=point_pentagon, angle=0, length=100, color=color)
    hexagon(point_hexagon, angle=0, length=100, color=color)

    break

sd.pause()

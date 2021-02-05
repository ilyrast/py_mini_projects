# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 600)


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


# TODO, пожалуйста, реализуйте функцию Смайлик =)

def smile(x_coord, y_coord, color):
    point_main = sd.get_point(x_coord, y_coord)
    radius_main = 50
    point_1 = sd.get_point(x_coord - 20, y_coord + 20)
    radius_1 = 5
    point_2 = sd.get_point(x_coord + 20, y_coord + 20)
    p1 = sd.get_point(x_coord - 25, y_coord - 20)
    p2 = sd.get_point(x_coord - 10, y_coord - 25)
    p3 = sd.get_point(x_coord + 10, y_coord - 25)
    p4 = sd.get_point(x_coord + 25, y_coord - 20)
    lines = p1, p2, p3, p4
    sd.circle(center_position=point_main, radius=radius_main, color=color)
    sd.circle(center_position=point_1, radius=radius_1, color=color)
    sd.circle(center_position=point_2, radius=radius_1, color=color)
    sd.lines(point_list=lines, color=color, closed=False, width=1)


for _ in range(10):
    x_coord = sd.random_number(0, 1200)
    y_coord = sd.random_number(0, 600)
    color = sd.COLOR_WHITE
    smile(x_coord, y_coord, color=color)

sd.pause()

# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
sd.resolution = (1200, 600)

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


# TODO, пожалуйста, реализуйте функцию Смайлик =)

for _ in range(10):
    x = sd.random_number(0, 1200)
    y = sd.random_number(0, 600)
    point_main = sd.get_point(x, y)
    radius_main = 50
    point_1 = sd.get_point(x-20, y+20)
    radius_1 = 5
    point_2 = sd.get_point(x+20, y+20)
    color = sd.COLOR_WHITE
    p1 = sd.get_point(x - 25, y - 20)
    p2 = sd.get_point(x - 10, y - 25)
    p3 = sd.get_point(x + 10, y - 25)
    p4 = sd.get_point(x + 25, y - 20)
    lines = p1, p2, p3, p4
    sd.circle(center_position=point_main, radius=radius_main, color=color)
    sd.circle(center_position=point_1, radius=radius_1, color=color)
    sd.circle(center_position=point_2, radius=radius_1, color=color)
    sd.lines(point_list=lines, color=color, closed=False, width=1)

sd.pause()

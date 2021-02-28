# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd




# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


# , пожалуйста, реализуйте функцию Смайлик =)

def smile():
    x_coord = 470
    y_coord = 230
    color = sd.COLOR_DARK_YELLOW
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



# зачёт!

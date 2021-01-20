# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


for y in range(0, 600, 100):
    for x in range(0, 1200, 100):
        point_low_1 = sd.get_point(x, y)
        point_high_1 = sd.get_point(x + 100, y + 50)
        point_low_2 = sd.get_point(x - 50, y + 50)
        point_high_2 = sd.get_point(x + 50, y + 100)
        sd.rectangle(point_low_1, point_high_1, color=sd.COLOR_DARK_ORANGE, width=2)
        sd.rectangle(point_low_2, point_high_2, color=sd.COLOR_DARK_ORANGE, width=2)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()

# зачёт!

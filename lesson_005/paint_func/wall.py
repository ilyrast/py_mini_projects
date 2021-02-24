# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
#
# sd.resolution = (1200, 600)
# # Нарисовать стену из кирпичей. Размер кирпича - 100х50
# # Использовать вложенные циклы for



def wall(x_start, x_end, y_start, y_end, color):
    for y in range(y_start, y_end, 100):
        for x in range(x_start, x_end, 100):
            point_low_1 = sd.get_point(x, y)
            point_high_1 = sd.get_point(x + 100, y + 50)
            point_low_2 = sd.get_point(x - 50, y + 50)
            point_high_2 = sd.get_point(x + 50, y + 100)
            sd.rectangle(point_low_1, point_high_1, color=color, width=2)
            sd.rectangle(point_low_2, point_high_2, color=color, width=2)


# wall(300, , 0, 200)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

# sd.pause()

# зачёт!

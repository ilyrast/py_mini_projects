# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(600, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(point, radius)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, radius, color):
    sd.circle(center_position=point, radius=radius, color=color)


# point = sd.get_point(100, 100)
# bubble(point=point, radius=50, color=sd.COLOR_RED)

# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1001, 100):
#     point = sd.get_point(x, 100)
#     bubble(point=point, radius=50, color=sd.COLOR_RED)


# Нарисовать три ряда по 10 пузырьков
# for y in range (100, 301, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, radius=50, color=sd.COLOR_RED)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    bubble(point=point, radius=50, color=sd.COLOR_RED)
sd.pause()

# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# point_triangle = sd.get_point(100, 150)
# point_squad = sd.get_point(600, 150)
# point_pentagon = sd.get_point(100, 400)
# point_hexagon = sd.get_point(600, 400)


# def triangle(point, angle, length):
#     new_point = point
#     for angle in range(angle + 0, angle + 361, 120):
#         v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
#         v.draw()
#         new_point = v.end_point
#
# def square(point, angle, length):
#     new_point = point
#     for angle in range(angle + 0, angle + 361, 90):
#         v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
#         v.draw()
#         new_point = v.end_point
#
# def pentagon(point, angle, length):
#     new_point = point
#     for angle in range(angle + 0, angle + 361, 72):
#         v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
#         v.draw()
#         new_point = v.end_point
#
# def hexagon(point, angle, length):
#     new_point = point
#     for angle in range(angle + 0, angle + 361, 60):
#         v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
#         v.draw()
#         new_point = v.end_point
#
#
# triangle(point=point_triangle, angle=0, length=100)
# square(point=point_squad, angle=0, length=100)
# pentagon(point=point_pentagon, angle=0, length=100)
# hexagon(point_hexagon, angle=0, length=100)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# зачёт первой части.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудьте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

def triangle(point, angle, length):
    draw_fig(point=point, angle=angle, length=length, angle_step=120)

def square(point, angle, length):
    draw_fig(point=point, angle=angle, length=length, angle_step=90)

def pentagon(point, angle, length):
    draw_fig(point=point, angle=angle, length=length, angle_step=72)

def hexagon(point, angle, length):
    draw_fig(point=point, angle=angle, length=length, angle_step=60)

def draw_fig (point, angle, length, angle_step):
    # TODO, пожалуйста, обратите внимание, сейчас в каждой фигуре рисуем на одну сторону больше.
    #  Предлагаю одним из параметров функции сделать "Количество сторон" и рассчитывать угол исходя из этого параметра =)
    #  Рисовать на 1 линию меньше векторами и последнюю простой линией. Таким образом в больших фигурах избежим разрыва.
    new_point = point
    for angle in range(angle + 0, angle + 361, angle_step):  # TODO + 0 лишний =)
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw()
        new_point = v.end_point

point_triangle = sd.get_point(100, 150)
point_squad = sd.get_point(600, 150)
point_pentagon = sd.get_point(100, 400)
point_hexagon = sd.get_point(600, 400)

triangle(point=point_triangle, angle=0, length=100)
square(point=point_squad, angle=0, length=100)
pentagon(point=point_pentagon, angle=0, length=100)
hexagon(point_hexagon, angle=0, length=100)

sd.pause()

# -*- coding: utf-8 -*-

import simple_draw as sd


def triangle(point, angle, length):
    new_point = point
    for angle in range(angle + 0, angle + 361, 120):
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw()
        new_point = v.end_point


def square(point, angle, length):
    new_point = point
    for angle in range(angle + 0, angle + 361, 90):
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw()
        new_point = v.end_point


def pentagon(point, angle, length):
    new_point = point
    for angle in range(angle + 0, angle + 361, 72):
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw()
        new_point = v.end_point


def hexagon(point, angle, length):
    new_point = point
    for angle in range(angle + 0, angle + 361, 60):
        v = sd.get_vector(start_point=new_point, angle=angle, length=length, width=3)
        v.draw()
        new_point = v.end_point


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

print("Возможные фигуры:")

figure = {
    '0': ("Треугольник", triangle),
    '1': ("Квадрат", square),
    '2': ("Пятиугольник", pentagon),
    '3': ("Шестиугольник", hexagon)
}

length = 100

middle_point = sd.get_point(sd.resolution[0] / 2 - length / 2, sd.resolution[1] / 2 - length / 2)

for key, value in figure.items():
    print(key, ':', value[0])
number = input()
while True:
    if number not in figure.keys():
        print('Введите корректный номер')
        number = input()
    else:
        fig = figure.get(number)[1]
        break
fig(point=middle_point, angle=0, length=length)

sd.pause()

# зачёт!

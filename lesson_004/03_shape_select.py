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

# TODO, предлагаю объединить словарь и список в один массив.
#  Ключём будет ввод пользователя в текстовом формате, а значением список из названия фигур и функции =)
figure = {0: "Треугольник", 1: "Квадрат", 2: "Пятиугольник", 3: "Шестиугольник"}

figure_list = (triangle, square, pentagon, hexagon)

# TODO, для запроса корректного ввода пользователя, предлагаю реализовать цикл while True.
#  Если ввод пользователя есть в словаре, создаём переменную с цветом и выходим из цикла =)
#  Проверить наличие ключа в словаре можно при помощи "in" =)
for key, value in figure.items():
    print(key, ':', value)

number = input()
number = int(number)

if number > 3 or number < 0:
    print('Неверный номер')

length = 100
middle_point = sd.get_point(sd.resolution[0]/2 - length/2, sd.resolution[1]/2 - length/2)
figure_list[number](point=middle_point, angle=0, length=length)

sd.pause()
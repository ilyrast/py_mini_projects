# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# def draw_branches(point, angle, length):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle-30, length=length, width=1)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point, angle=angle+30, length=length, width=1)
#     v2.draw()
#     next_point_1 = v1.end_point
#     next_point_2 = v2.end_point
#     next_angle_1 = angle - 30
#     next_angle_2 = angle + 30
#     new_length = length * 0.75
#     draw_branches(point=next_point_1, angle=next_angle_1, length=new_length)
#     draw_branches(point=next_point_2, angle=next_angle_2, length=new_length)
#
# root_point = sd.get_point(300, 30)
#
# v = sd.get_vector(start_point=root_point, angle=90, length=100, width=1)
# v.draw()
#
# draw_branches(point=v.end_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла v= sd.get_vector(start_point=point, angle=angle, length=length, width=3)ветвей в пределах 40% от 30-ти градусов (28, 42)
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75 (60, 90)
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_branches(point, angle, length):
    if length < 5:
        return
    # TODO, функция должна рисовать только 1 веточку и запускать себя дважды =)
    v1 = sd.get_vector(start_point=point, angle=angle - 30, length=length, width=1)
    v1.draw()
    v2 = sd.get_vector(start_point=point, angle=angle + 30, length=length, width=1)
    v2.draw()
    next_point_1 = v1.end_point
    next_point_2 = v2.end_point
    next_angle_1 = angle - sd.random_number(28, 42)
    next_angle_2 = angle + sd.random_number(28, 42)
    new_length = length * sd.random_number(60, 90) / 100
    draw_branches(point=next_point_1, angle=next_angle_1, length=new_length)
    draw_branches(point=next_point_2, angle=next_angle_2, length=new_length)


root_point = sd.get_point(300, 30)

v = sd.get_vector(start_point=root_point, angle=90, length=100, width=1)  # TODO, лишний код =)
v.draw()  # TODO, лишний код =)

draw_branches(point=v.end_point, angle=90, length=100)

sd.pause()

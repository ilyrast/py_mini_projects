# -*- coding: utf-8 -*-

import simple_draw as sd
# from .rainbow import rainbow
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные



# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# snow_list = []
# #len_compare = []
#
# for i in range(N):
#     x = sd.random_number(10, sd.resolution[0])
#     len_i = sd.random_number(10, 100)
#     #  переменная len_compare и цикл получились лишними =)
#     # почему лишними? если убрать цикл, то не все длины будут раные
#    #n_compare.append(len_i)
#     snow_list.append([x, sd.resolution[1] - 10, len_i])
#
# while True:
#     sd.clear_screen()
#     for index, l_list in enumerate(snow_list):
#         coord_x, coord_y, length = l_list
#         point = sd.get_point(coord_x, coord_y)
#         sd.snowflake(center=point, length=length)
#         if coord_y < 10:
#             coord_y = sd.resolution[1] - 10
#         snow_list[index] = ([coord_x, coord_y - 30, length])
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

def snow_rain ():
    count = 10
    coord_start_x = 10
    coord_end_x = 180
    coord_start_y = 450
    coord_end_y = 700
    snow_list = []

    for i in range(count):
        x = sd.random_number(coord_start_x, coord_end_x)
        y = sd.random_number(coord_start_y, coord_end_y)
        len_i = sd.random_number(15, 20)
        snow_list.append([x, y, len_i])

    while True:
        sd.start_drawing()
        for index, l_list in enumerate(snow_list):
            coord_x, coord_y, length = l_list
            point = sd.get_point(coord_x, coord_y)
            sd.snowflake(center=point, length=length, color=sd.background_color)
            if coord_y < 85:
                sd.snowflake(center=point, length=length)
                snow_list[index] = ([
                    sd.random_number(coord_start_x, coord_end_x),
                    sd.random_number(coord_start_y, coord_end_y),
                    sd.random_number(15, 20)
                ])
            else:
                deviation = sd.random_number(-5, 5)
                snow_list[index] = ([coord_x + deviation, coord_y - 10, length])
                point_1 = sd.get_point(coord_x + deviation, coord_y - 10)
                sd.snowflake(center=point_1, length=length)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break




# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

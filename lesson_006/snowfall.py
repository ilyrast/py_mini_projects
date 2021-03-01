# -*- coding: utf-8 -*-

import simple_draw as sd

snow_list = []
falled_snow_list = []


def snow_create(N):
    global snow_list
    for i in range(N):
        x = sd.random_number(10, sd.resolution[0])
        y = sd.random_number(sd.resolution[1] - 10, sd.resolution[1])
        len_i = sd.random_number(10, 35)
        snow_list.append([x, y, len_i])


def snow_paint():
    global snow_list
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        point = sd.get_point(coord_x, coord_y)
        sd.snowflake(center=point, length=length, color=sd.background_color)
    # TODO, запуск другой функции лишний.
    #  Эта функция должна рисовать или белый цветом или цветом фона.
    #  Возможно, стоит добавить параметр в функцию - "цвет"
    deviation()
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        point_1 = sd.get_point(coord_x, coord_y)
        sd.snowflake(center=point_1, length=length)


def check_fall():
    global snow_list
    global falled_snow_list
    # TODO, таким образом мы контролируем падение только одной снежинки.
    #  А если упадёт несколько?
    #  Возможно стоит возвращать список снежинок вместо True и False.
    #  В таком случае, основной цикл немного измениться.
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        if coord_y < -15:
            falled_snow_list.append(index)
        else:
            return False
        return True


def snow_delete():
    global falled_snow_list
    global snow_list
    count = len(falled_snow_list)
    # TODO, предлагаю идти в цикле по списку falled_snow_list и удалять снежинки из snow_list.
    #  Если check_fall будет возвращать список упавших снежинок, то в этой функции должен быть параметр - список упавших снежинок.
    #  В таком случае falled_snow_list не нужно делать глобальной =)
    for i in range(count):
        snow_list.pop(falled_snow_list[i])
    falled_snow_list.clear()
    return count


def deviation():
    global snow_list
    for index, l_list in enumerate(snow_list):
        deviation = sd.random_number(-20, 20)
        snow_list[index] = ([l_list[0] + deviation, l_list[1] - 10, l_list[2]])

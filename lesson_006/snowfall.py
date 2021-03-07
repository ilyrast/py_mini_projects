# -*- coding: utf-8 -*-

import simple_draw as sd

snow_list = []
falled_snow_list = []  # переменная не глобальная =)


def snow_create(N):
    global snow_list
    for i in range(N):
        x = sd.random_number(10, sd.resolution[0])
        y = sd.random_number(sd.resolution[1] - 10, sd.resolution[1])
        len_i = sd.random_number(10, 35)
        snow_list.append([x, y, len_i])


def snow_paint(color):
    global snow_list
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        point = sd.get_point(coord_x, coord_y)
        sd.snowflake(center=point, length=length, color=color)


def check_fall():
    global snow_list
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        if coord_y < -15:
            falled_snow_list.append(index)
        return falled_snow_list


def snow_delete(list):
    global snow_list
    count = len(list)
    for check in list:
        snow_list.pop(list[check])
    falled_snow_list.clear()  # лишнее действие.
    return count


def deviation():
    global snow_list
    for index, l_list in enumerate(snow_list):
        deviation = sd.random_number(-20, 20)
        snow_list[index] = ([l_list[0] + deviation, l_list[1] - 10, l_list[2]])

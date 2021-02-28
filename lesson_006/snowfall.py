# -*- coding: utf-8 -*-

import simple_draw as sd

snow_list = []
falled_snow_list =[]

def snow_create(N):
    for i in range(N):
        x = sd.random_number(10, sd.resolution[0])
        y = sd.random_number(sd.resolution[1] - 10, sd.resolution[1])
        len_i = sd.random_number(10, 35)
        snow_list.append([x, y, len_i])

def snow_paint_background():
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        point = sd.get_point(coord_x, coord_y)
        sd.snowflake(center=point, length=length, color=sd.background_color)

def check_fall():
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        if coord_y < -15:
            falled_snow_list.append(index)
        else:
            return False
        return True

def snow_delete():
    count = len(falled_snow_list)
    for i in range(count):
        snow_list.pop(falled_snow_list[i])
    falled_snow_list.clear()
    return count

def deviation():
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        deviation = sd.random_number(-20, 20)
        snow_list[index] = ([coord_x + deviation, coord_y - 10, length])


def snow_paint():
    for index, l_list in enumerate(snow_list):
        coord_x, coord_y, length = l_list
        point_1 = sd.get_point(coord_x, coord_y)
        sd.snowflake(center=point_1, length=length)

    # if sd.user_want_exit():
    #     break

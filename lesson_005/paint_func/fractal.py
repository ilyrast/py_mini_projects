# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_branches(point = sd.get_point(900, 80), angle = 90, length = 70):
    if length < 5:
        return
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v.draw()
    next_point = v.end_point
    next_angle_1 = angle - sd.random_number(28, 42)
    next_angle_2 = angle + sd.random_number(28, 42)
    new_length = length * sd.random_number(60, 90) / 100
    draw_branches(point=next_point, angle=next_angle_1, length=new_length)
    draw_branches(point=next_point, angle=next_angle_2, length=new_length)



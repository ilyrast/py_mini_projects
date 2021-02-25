# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

def chel(x_coord, y_coord, color):
    left_leg = sd.get_point(1050, 80)
    right_leg = sd.get_point(1150, 80)
    body_low = sd.get_point(1100, 130)
    body_top = sd.get_point(1100, 180)
    body_hands = sd.get_point(1100, 165)
    left_hand = sd.get_point(1150, 130)
    right_hand = sd.get_point(1050, 130)

    point_main = sd.get_point(x_coord, y_coord)
    radius_main = 50
    point_1 = sd.get_point(x_coord - 20, y_coord + 20)
    radius_1 = 5
    point_2 = sd.get_point(x_coord + 20, y_coord + 20)
    p1 = sd.get_point(x_coord - 25, y_coord - 20)
    p2 = sd.get_point(x_coord - 10, y_coord - 25)
    p3 = sd.get_point(x_coord + 10, y_coord - 25)
    p4 = sd.get_point(x_coord + 25, y_coord - 20)
    lines = p1, p2, p3, p4
    sd.circle(center_position=point_main, radius=radius_main, color=color)
    sd.circle(center_position=point_1, radius=radius_1, color=color)
    sd.circle(center_position=point_2, radius=radius_1, color=color)
    sd.lines(point_list=lines, color=color, closed=False, width=1)

    sd.line(start_point=left_leg, end_point=body_low, color=sd.COLOR_DARK_YELLOW, width=1)  # Левая нога
    sd.line(start_point=right_leg, end_point=body_low, color=sd.COLOR_DARK_YELLOW, width=1)  # Правая нога
    sd.line(start_point=body_low, end_point=body_top, color=sd.COLOR_DARK_YELLOW, width=1)  # Тело
    sd.line(start_point=body_hands, end_point=left_hand, color=sd.COLOR_DARK_YELLOW, width=1)  # Левая рука
    sd.line(start_point=body_hands, end_point=right_hand, color=sd.COLOR_DARK_YELLOW, width=1)  # Правая рука

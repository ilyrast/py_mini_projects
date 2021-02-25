# -*- coding: utf-8 -*-

import simple_draw as sd
from .wall import wall
def house():
    point_list_1 = []

    point_list_1.append(sd.get_point(230, 380))
    point_list_1.append(sd.get_point(475, 480))
    point_list_1.append(sd.get_point(720, 380))
    left_bot = sd.get_point(0, 0)
    right_top = sd.get_point(1200, 80)
    start_point = sd.get_point(250, 80)
    end_point = sd.get_point(700, 80)
    end_point_1 = sd.get_point(700, 380)

    sd.rectangle(left_bottom=left_bot, right_top=right_top, color=sd.COLOR_DARK_ORANGE, width=0)  # Земля

    v1 = sd.vector(start=start_point, angle=90, length=300, color=sd.COLOR_YELLOW, width=2)
    v2 = sd.vector(start=end_point, angle=90, length=300, color=sd.COLOR_YELLOW, width=2)
    v3 = sd.vector(start=end_point_1, angle=180, length=450, color=sd.COLOR_YELLOW, width=2)
    v4 = sd.vector(start=start_point, angle=0, length=450, color=sd.COLOR_YELLOW, width=2)

    wall(x_start=300, x_end=650, y_start=80, y_end=380, color=sd.COLOR_YELLOW)

    sd.polygon(point_list=point_list_1, color=sd.COLOR_RED, width=0)
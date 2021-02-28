# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

def rainbow():
    x_rain = 350
    y_rain = -200
    radius = 1100
    width = 30

    rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
    y_list = []
    for y in range(y_rain, y_rain + 210, 30):
        y_list.append(y)
    for index, color in enumerate(rainbow_colors):
        point = sd.get_point(x_rain, y_list[index])
        sd.circle(center_position=point, radius=radius, color=color, width=width)







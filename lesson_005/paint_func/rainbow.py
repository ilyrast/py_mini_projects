# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

def rainbow(x, y, radius, width):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    y = y
    for i in range(0, 7):
        color = rainbow_colors[i]
        point = sd.get_point(x, y)
        sd.circle(center_position=point, radius=radius, color=color, width=width)
        y += 30




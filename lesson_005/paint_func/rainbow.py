# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

def rainbow(x, y, radius, width):
    rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
    y_list = []
    for y in range(y, y + 210, 30):
        y_list.append(y)
        for index, color in enumerate(rainbow_colors):
            point = sd.get_point(x, y_list[index])
            sd.circle(center_position=point, radius=radius, color=color, width=width)
            if index+1 == 7:
                rainbow_colors[index] = rainbow_colors[0]
            else:
                rainbow_colors[index] = rainbow_colors[index+1]
        sd.sleep(0.3)







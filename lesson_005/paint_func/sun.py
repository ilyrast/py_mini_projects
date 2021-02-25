# -*- coding: utf-8 -*-

import simple_draw as sd


def sun():
    position = sd.get_point(275, 700)
    radius = 50
    sd.circle(center_position=position, radius=radius, color=sd.COLOR_YELLOW, width=0)
    for i in range(0, 360, 36):
        sd.vector(start=position, angle=i, length=radius+35, color=sd.COLOR_YELLOW, width=3)


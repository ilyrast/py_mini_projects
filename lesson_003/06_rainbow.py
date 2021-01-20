# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

y = 50
z = 450
for i in range(0, 7):
    color = rainbow_colors[i]
    point_low = sd.get_point(50, y)
    point_high = sd.get_point(350, z)
    sd.line(start_point=point_low, end_point=point_high, width=4, color=color)
    y += 5
    z += 5

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

y = -300
for i in range(0, 7):
    color = rainbow_colors[i]
    point = sd.get_point(600, y)
    sd.circle(center_position=point, radius=400, color=color, width=30)
    y += 30
sd.pause()

# зачёт!

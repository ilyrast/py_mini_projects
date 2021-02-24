# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from paint_func.wall import wall
from paint_func.snowfall import snow
from paint_func.fractal import draw_branches
from paint_func.rainbow import rainbow
from paint_func.smile import smile
from paint_func.sun import sun

sd.resolution = (1200, 800)

point_list_1 = []

point_list_1.append(sd.get_point(230, 380))
point_list_1.append(sd.get_point(475, 480))
point_list_1.append(sd.get_point(720, 380))

right_top = sd.get_point(1200, 80)
start_point = sd.get_point(250, 80)
end_point = sd.get_point(700, 80)
end_point_1 = sd.get_point(700, 380)
left_bot = sd.get_point(0, 0)
left_leg = sd.get_point(1050, 80)
right_leg = sd.get_point(1150, 80)
body_low = sd.get_point(1100, 130)
body_top = sd.get_point(1100, 180)
body_hands = sd.get_point(1100, 165)
left_hand = sd.get_point(1150, 130)
right_hand = sd.get_point(1050, 130)
root_point = sd.get_point(900, 80)
sun_position = sd.get_point(275, 700)


sd.rectangle(left_bottom=left_bot, right_top=right_top, color=sd.COLOR_DARK_ORANGE, width=0)  # Земля

v1 = sd.vector(start=start_point, angle=90, length=300, color=sd.COLOR_YELLOW, width=2)
v2 = sd.vector(start=end_point, angle=90, length=300, color=sd.COLOR_YELLOW, width=2)
v3 = sd.vector(start=end_point_1, angle=180, length=450, color=sd.COLOR_YELLOW, width=2)
v4 = sd.vector(start=start_point, angle=0, length=450, color=sd.COLOR_YELLOW, width=2)

wall(x_start=300, x_end=650, y_start=80, y_end=380, color=sd.COLOR_YELLOW)  # Стена

sd.polygon(point_list=point_list_1, color=sd.COLOR_RED, width=0)  # Крыша

rainbow(350, -200, radius=1100, width=30)  # Радуга

sun(position=sun_position, radius=50)  # Солнце

smile(1100, 230, sd.COLOR_DARK_YELLOW)  # Голова
sd.line(start_point=left_leg, end_point=body_low, color=sd.COLOR_DARK_YELLOW, width=1)  # Левая нога
sd.line(start_point=right_leg, end_point=body_low, color=sd.COLOR_DARK_YELLOW, width=1)  # Правая нога
sd.line(start_point=body_low, end_point=body_top, color=sd.COLOR_DARK_YELLOW, width=1)  # Тело
sd.line(start_point=body_hands, end_point=left_hand, color=sd.COLOR_DARK_YELLOW, width=1)  # Левая рука
sd.line(start_point=body_hands, end_point=right_hand, color=sd.COLOR_DARK_YELLOW, width=1)  # Правая рука

draw_branches(point=root_point, angle=90, length=70)  # Дерево

snow(count=10, coord_start_x=10, coord_end_x=180, coord_start_y=450, coord_end_y=700)  # Снегопад



sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

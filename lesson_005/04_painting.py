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
from paint_func.house import house
from paint_func.snowfall import snow_rain
from paint_func.fractal import draw_branches
from paint_func.smile import chel
from paint_func.sun import sun

sd.resolution = (1200, 800)



# TODO, пожалуйста, перенесите весь код для отрисовки домика в один модуль.
#  Создайте 1 функцию, которая будет рисовать домик, импортируйте в этот модуль и запустите =)


right_top = sd.get_point(1200, 80)
start_point = sd.get_point(250, 80)
end_point = sd.get_point(700, 80)
end_point_1 = sd.get_point(700, 380)
left_bot = sd.get_point(0, 0)
root_point = sd.get_point(900, 80)
sun_position = sd.get_point(275, 700)


sd.rectangle(left_bottom=left_bot, right_top=right_top, color=sd.COLOR_DARK_ORANGE, width=0)  # Земля

sun(position=sun_position, radius=50)  # Солнце

house(start_point=start_point, end_point=end_point, end_point_1=end_point_1)

chel(1100,
     230,                       #человек
     sd.COLOR_DARK_YELLOW)


draw_branches(point=root_point, angle=90, length=70)  # Дерево

snow_rain(count=10,
          coord_start_x=10,
          coord_end_x=180,
          coord_start_y=450,
          coord_end_y=700,                      # Снегопад + Радуга
          x_rain=350,
          y_rain=-200,
          radius=1100,
          width=30)

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

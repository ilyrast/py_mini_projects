# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import snow_create
from snowfall import snow_paint
from snowfall import check_fall
from snowfall import snow_delete
from snowfall import deviation
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
snow_create(5)
while True:
    sd.start_drawing()
    snow_paint(color=sd.background_color)
    deviation()
    snow_paint(color=sd.COLOR_WHITE)
    snow_create(snow_delete(list=check_fall()))
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

first_song_time = violator_songs[3][1]
first_song_time = round(first_song_time, 2)

second_song_time = violator_songs[5][1]
second_song_time = round(second_song_time, 2)

third_song_time = violator_songs[-1][1]
third_song_time = round(third_song_time, 2)

# Или лучше так. В одно действие с 1 переменной =)
example_all_song = round(
    violator_songs[3][1]
    + violator_songs[5][1]
    + violator_songs[-1][1]
    , 2)

time = first_song_time + second_song_time + third_song_time
time = round(time, 2)

print('Три песни звучат', time, 'минут')

# Есть словарь песен группы Yellow со временем звучания с точностью до долей минут
pocket_universe_songs = {
    'Solar Driftwood': 1.85,
    'Celsius': 5.98,
    'More': 6.65,
    'On Track': 5.55,
    'Monolith': 6.35,
    'To the Sea': 5.77,
    'Magnetic': 5.88,
    'Liquid Mountain': 2.97,
    'Pan Blue': 5.52,
    'Resistor': 7.22,
    'Beyond Mirrors': 5.82,
}

# Распечатайте общее время звучания трех песен: 'On Track', 'To the Sea' и 'Beyond Mirrors'
#   А другие три песни звучат приблизительно ХХХ минут

first_song_time = pocket_universe_songs['On Track']
first_song_time = round(first_song_time, 2)

second_song_time = pocket_universe_songs['To the Sea']
second_song_time = round(second_song_time, 2)

third_song_time = pocket_universe_songs['Beyond Mirrors']
third_song_time = round(third_song_time, 2)

time = first_song_time + second_song_time + third_song_time

print('А другие три песни звучат приблизительно', time, 'минут')
# TODO, Илья, пожалуйста, обратите внимание, в последнем print необходимо округлить с помощь round до целых.
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

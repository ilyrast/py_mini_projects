#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

link_lamps = store[goods['Лампа']]
lamps_cost = link_lamps[0]['quantity'] * link_lamps[0]['price']
print('Лампа -', link_lamps[0]['quantity'], 'шт, стоимость', lamps_cost, 'руб')
# или проще (/сложнее ?)


lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.



link_table = store[goods['Стол']]
table_cost_1 = link_table[0]['quantity'] * link_table[0]['price']
table_cost_2 = link_table[1]['quantity'] * link_table[1]['price']
table_quantity = link_table[0]['quantity'] + link_table[1]['quantity']
table_cost = table_cost_1 + table_cost_2

link_chair = store[goods['Стул']]
chair_cost_1 = link_chair[0]['quantity'] * link_chair[0]['price']
chair_cost_2 = link_chair[1]['quantity'] * link_chair[1]['price']
chair_cost_3 = link_chair[2]['quantity'] * link_chair[2]['price']
chair_quantity_1 = link_chair[0]['quantity'] + link_chair[1]['quantity']
chair_quantity = chair_quantity_1 + link_chair[2]['quantity']
chair_cost = chair_cost_1 + chair_cost_2 + chair_cost_3

link_sofa = store[goods['Диван']]
sofa_cost_1 = link_sofa[0]['quantity'] * link_sofa[0]['price']
sofa_cost_2 = link_sofa[1]['quantity'] * link_sofa[1]['price']
sofa_quantity = link_sofa[0]['quantity'] + link_sofa[1]['quantity']
sofa_cost = sofa_cost_1 + sofa_cost_2

print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################

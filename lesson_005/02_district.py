# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as f0
from district.central_street.house1.room2 import folks as f1
from district.central_street.house2.room1 import folks as f2
from district.central_street.house2.room2 import folks as f3
s = ', '
name_list = []
# TODO, а как добавить все элементы одного списка в другой за один списковый метод без цикла? =)
for index, name in enumerate(f0):
    name_list.append(name)
for index, name in enumerate(f1):
    name_list.append(name)
for index, name in enumerate(f2):
    name_list.append(name)
for index, name in enumerate(f3):
    name_list.append(name)
print('На районе живут:', s.join(name_list))
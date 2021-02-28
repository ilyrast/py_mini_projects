# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as f0
from district.central_street.house1.room2 import folks as f1
from district.central_street.house2.room1 import folks as f2
from district.central_street.house2.room2 import folks as f3
from district.soviet_street.house1.room1 import folks as f4
from district.soviet_street.house1.room2 import folks as f5
from district.soviet_street.house2.room1 import folks as f6
from district.soviet_street.house2.room2 import folks as f7

s = ', '
name_list = []

name_list.extend(f0)
name_list.extend(f1)
name_list.extend(f2)
name_list.extend(f3)
name_list.extend(f4)
name_list.extend(f5)
name_list.extend(f6)
name_list.extend(f7)

print('На районе живут:', s.join(name_list))
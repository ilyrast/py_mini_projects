#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['father', 'mother', 'gr_father', 'gr_mother']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['father', '190'],
    ['mother', '170'],
    ['gr_father', '178']
]

print('Рост отца -', my_family_height[0][1], 'см')
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см


father_height = my_family_height[0][1]
mother_height = my_family_height[1][1]
gr_father = my_family_height[2][1]
summary_height = int(father_height) + int(mother_height) + int(gr_father)

print('Общий рост семьи -', summary_height, 'см')

# зачёт!

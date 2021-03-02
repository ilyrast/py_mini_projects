import simple_draw as sd

Number_list = []


def rand_number():
    global Number_list
    Number_set = set()
    Number_set.add(str(sd.random_number(1, 9)))
    while len(Number_set) < 4:
        Number_set.add(str(sd.random_number(0, 9)))
    Number_list = list(Number_set)


def check_number(input_number):
    global Number_list
    bulls = 0
    cows = 0
    input_number = list(input_number)
    for index, i in enumerate(input_number):
        if i in Number_list:
            if index == Number_list[index]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def gameover(bulls):
    if bulls == 4:
        Number_list.clear()
        return True
    else:
        return False


def check_input(number):
    if len(set(number)) != 4:
        print('Число должно содержать четыре разные цифры ')
    elif '0' in list(number)[0]:
        print('Первым не должен быть 0')
    elif not number.isdigit():
        print('Неправильный формат ввода')
    else:
        return True

rand_number()
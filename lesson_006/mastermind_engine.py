import simple_draw as sd

Number_set = set()


def rand_number():
    global Number_set
    while len(Number_set) < 4:
        Number_set.add(str(sd.random_number(1, 9)))
    Number_set = list(Number_set)


def check_number(input_number):
    global Number_set
    bulls = 0
    cows = 0
    input_number = list(input_number)
    for i in input_number:
        if i in Number_set:
            if Number_set.index(i) == input_number.index(i):
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def same_in_list(list_1, list_2):
    k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if list_1[i] == list_2[j]:
                k += 1
    return (k)


def gameover(bulls):
    if bulls == 4:
        Number_set.clear()
        return True
    else:
        return False


def check_input(number):
    if len(set(number)) != 4:
        print('Число должно содержать четыре разные цифры ')
    elif '0' in set(number):
        print('Первым не должен быть 0')
    elif not number.isdigit():
        print('Неправильный формат ввода')
    else:
        return True

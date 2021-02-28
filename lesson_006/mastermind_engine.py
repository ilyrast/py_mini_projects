import simple_draw as sd


# TODO, пожалуйста, поправьте названия переменных ои одной буквы.
#  Названия должны отражать суть их содержания =)

N = []

def rand_number():
    # TODO, возможно сможем решить только 1 циклом while? =)
    # TODO, если в функции используем глобальную переменную, обязательно об этом указываем в начале функции.
    for i in range(4):
        j = sd.random_number(1, 9)
        while N.count(j) == True:
            j = sd.random_number(1, 9)
        N.append(j)

def check_number(input_list):
    # TODO, если в функции используем глобальную переменную, обязательно об этом указываем в начале функции.

    bulls = 0
    cows = 0
    # TODO, было бы правильней идти в цикле по одному из чисел.
    for i in range(4):
        if input_list[i] == N[i]:
            bulls += 1
        if N.count(input_list[i]) != 0:
            cows += 1
    cows -= bulls
    return (bulls, cows)

def same_in_list(list_1, list_2):
    k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if list_1[i] == list_2[j]:
                k += 1
    return(k)

def gameover(bulls):
    if bulls == 4:
        N.clear()
        return True
    else:
        return False
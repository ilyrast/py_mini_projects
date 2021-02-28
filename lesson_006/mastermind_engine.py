import simple_draw as sd

N = [4, 5, 8, 1]

def rand_number():
    for i in range(4):
        j = sd.random_number(1, 9)
        while N.count(j) == True:
            j = sd.random_number(1, 9)
        N.append(j)

def check_number(input_list):
    # в цикле от 1 до 4
    # if число на позиции [i] списка 1  = числу на позиции [i] списка 2
    # увеличиваю переменную bulls
    # elif число из списка 1 есть в списке 2
    # увеличиваю переменную cows
    # else вывожу пустой словарь
    bulls = 0
    cows = 0
    for i in range(4):
        if input_list[i] == N[i]:
            bulls += 1
    cows = same_in_list(list_1=input_list, list_2=N)
    return(bulls, cows)

def same_in_list(list_1, list_2):
    k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if list_1[i] == list_2[j]:
                k += 1
    return(k)


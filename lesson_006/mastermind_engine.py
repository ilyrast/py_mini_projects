import simple_draw as sd

N = []  # добавлять случайные числа с проверкой на наличие в списке


def rand_number():
    for i in range(4):
        j = sd.random_number(1, 9)
        while N.count(j) == True:
            j = sd.random_number(1, 9)
        N.append(j)  # extend??


def check_number():
    pass


rand_number()

print(N)

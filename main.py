import random
import string


def generate_num(m):
    """
    Генератор неповторяющихся комбинаций цифр.
    """
    pas = random.choice(passwd)
    while m - 1 > 0:
        a = random.choice(passwd)
        if a not in pas:
            pas += a
            m -= 1
    return pas


def massive(number, vvod):
    """
    Функция, которая по числу возвращает массив цифр в том порядке, в котором они указаны.
    """

    for i in range(4):
        if bullscows(number, vvod)[0] > max(history, key=lambda x: x[1])[0]:
            if number[i] == vvod[i]:
                lstbull[i] = number[i]
            elif number[i] != vvod[i] and number[i] in vvod:
                lstbull[i] = '*'
                if number[i] not in lstcow:
                    lstcow.append(number[i])
        if number[i] in lstbull and number[i] in lstcow:
            lstcow.remove(number[i])
    print(f'Отладка massive. Быки {lstbull}, коровы {lstcow}')
    return lstbull, lstcow


def bullscows(number, vvod):
    """
    Функция, которая принимает два массива цифр: цифры загаданного числа
    и цифры из попытки отгадать — и считает по ним число быков и коров.
    """
    bulls = cows = 0
    for i in range(4):
        if number[i] == vvod[i]:
            bulls += 1
        elif number[i] in vvod:
            cows += 1
    return [bulls, cows]


def checkpass(ps):
    """
    Функция, которая проверяет, подходит ли новое «загаданное» число под историю уже данных ответов.
    """
    bull, cow = ps[0], ps[1]
    if cow:  # Если были "коровы", обязательно используем эти цифры.
        if len(cow) <= 4:
            ps = list(generate_num(bull.count('*')))
            # print(f'Проверка {set(cow)}, {set(ps)}, {set(bull) - set("*")}')
            # print(f'Массивы {set(cow) <= set(ps)}, {(set(bull) - set("*")) <= set(ps)}')
            while not (set(cow) <= set(ps) and not (set(bull) - set("*")) <= set(ps)):  # Пока не содержит "коров".
                ps = list(generate_num(bull.count('*')))  # Длина пароля по кол-ву символов '*'
                print(f'Новый список для генерации числа, содержащий коров, но не содержащий быков {ps}')
            for i in range(len(bull)):
                if bull[i] == '*':
                    bull[i] = ps.pop()
        else:
            random.shuffle(cow)
            bull = cow.copy()
    else:  # Если не было "коров".
        ps = list(set(passwd) - set(cow))
        while '*' in bull:
            for i in range(4):
                tmp = random.choice(ps)
                if tmp not in bull and bull[i] == '*':
                    bull[i] = tmp
    print(f'Отладка сheckpass. Новое число {bull}')
    return bull


lstcow = []
lstbull = ['*'] * 4
s = 1  # Счетчик попыток.
history = [(0, 0, 0)]  # Массив хранения истории.
passwd = string.digits  # Строка для генерации чисел.
num = list(generate_num(4))  # Загадываем число.
print(f'Загаданное число в список {num}')
vod = None
while vod != num:
    vod = list(input('Попытка {}\n'.format(s)))
    proverka = bullscows(num, vod)
    print(f'Быков {proverka[0]}, коров {proverka[1]}')
    history.append((s, proverka[0], proverka[1]))
    print(f'Номер попытки, max число быков в попытке {max(history, key=lambda x: x[1])}')
    num = checkpass(massive(num, vod))
    s += 1
